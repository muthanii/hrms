import frappe
from frappe.utils import getdate

from hrms.controllers.employee_reminders import (
	BIRTHDAY_REMINDERS_LAST_SENT_KEY,
	WORK_ANNIVERSARY_REMINDERS_LAST_SENT_KEY,
)

OLD_DAILY_JOBS = {
	"hrms.controllers.employee_reminders.send_birthday_reminders": BIRTHDAY_REMINDERS_LAST_SENT_KEY,
	"hrms.controllers.employee_reminders.send_work_anniversary_reminders": WORK_ANNIVERSARY_REMINDERS_LAST_SENT_KEY,
}


def execute():
	# if the old daily job already sent today's reminders, record that so the new hourly job
	# doesn't send them again; if it hasn't run yet today, leave the hourly job to send them
	today = getdate()
	for method, last_sent_key in OLD_DAILY_JOBS.items():
		last_execution = frappe.db.get_value("Scheduled Job Type", {"method": method}, "last_execution")
		if last_execution and getdate(last_execution) == today:
			frappe.db.set_default(last_sent_key, str(today))
