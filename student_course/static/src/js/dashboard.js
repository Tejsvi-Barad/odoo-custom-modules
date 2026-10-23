
/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class StudentCourseDashboard extends Component {
    static template = "student_course.Dashboard";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");

        this.state = useState({
            loading: true,
            error: false,
            students: 0,
            courses: 0,
            enrollments: 0,
            totalFees: 0,
            statuses: [],
            courseStats: [],
        });

        onWillStart(() => this.loadDashboard());
    }

    async loadDashboard() {
        this.state.loading = true;
        this.state.error = false;

        try {
            const [studentCount, courses, enrollments] =
                await Promise.all([
                    this.orm.searchCount(
                        "student.course.student",
                        []
                    ),
                    this.orm.searchRead(
                        "student.course.course",
                        [],
                        ["name", "fees"]
                    ),
                    this.orm.searchRead(
                        "student.course.enrollment",
                        [],
                        ["course_id", "status"]
                    ),
                ]);

            const statusLabels = {
                draft: "Draft",
                enrolled: "Enrolled",
                completed: "Completed",
                cancelled: "Cancelled",
            };

            const statusCounts = {
                draft: 0,
                enrolled: 0,
                completed: 0,
                cancelled: 0,
            };

            const courseCounts = {};

            // Initialize enrollment count for each course.
            for (const course of courses) {
                courseCounts[course.name] = 0;
            }

            // Count enrollment statuses and course-wise enrollments.
            for (const enrollment of enrollments) {
                const status = enrollment.status;

                if (
                    Object.prototype.hasOwnProperty.call(
                        statusCounts,
                        status
                    )
                ) {
                    statusCounts[status]++;
                }

                if (enrollment.course_id) {
                    const courseName = enrollment.course_id[1];

                    courseCounts[courseName] =
                        (courseCounts[courseName] || 0) + 1;
                }
            }

            const statusTotal = enrollments.length;

            const maxCourseCount = Math.max(
                1,
                ...Object.values(courseCounts)
            );

            // Update dashboard summary cards.
            this.state.students = studentCount;
            this.state.courses = courses.length;
            this.state.enrollments = enrollments.length;

            // Sum of fees for all course records.
            // This is not the amount of money collected.
            this.state.totalFees = courses.reduce(
                (total, course) =>
                    total + (Number(course.fees) || 0),
                0
            );

            // Prepare enrollment status chart data.
            this.state.statuses = Object.entries(
                statusCounts
            ).map(([key, count]) => ({
                name: statusLabels[key],
                count: count,
                percentage: statusTotal
                    ? (count / statusTotal) * 100
                    : 0,
            }));

            // Prepare course-wise enrollment chart data.
            this.state.courseStats = Object.entries(
                courseCounts
            ).map(([name, count]) => ({
                name: name,
                count: count,
                percentage:
                    (count / maxCourseCount) * 100,
            }));

        } catch (error) {
            console.error(
                "Student Course Dashboard Error:",
                error
            );

            this.state.error = true;

        } finally {
            this.state.loading = false;
        }
    }

    // Format fees in Indian Rupees.
    formatCurrency(amount) {
        return (Number(amount) || 0).toLocaleString(
            "en-IN",
            {
                style: "currency",
                currency: "INR",
                maximumFractionDigits: 0,
            }
        );
    }

    // Open Students list.
    openStudents() {
        this.action.doAction(
            "student_course.action_student"
        );
    }

    // Open Courses list.
    openCourses() {
        this.action.doAction(
            "student_course.action_course"
        );
    }

    // Open Enrollments list.
    openEnrollments() {
        this.action.doAction(
            "student_course.action_enrollment"
        );
    }

    // Refresh dashboard data.
    async refreshDashboard() {
        await this.loadDashboard();
    }
}

registry.category("actions").add(
    "student_course_dashboard",
    StudentCourseDashboard
);
