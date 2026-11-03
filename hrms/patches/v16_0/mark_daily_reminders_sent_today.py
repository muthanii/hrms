import frappe
from frappe.utils import nowdate

from hrms.controllers.employee_reminders import (
	BIRTHDAY_REMINDERS_LAST_SENT_KEY,
	WORK_ANNIVERSARY_REMINDERS_LAST_SENT_KEY,
)


def execute():
	# the old daily jobs have already sent today's reminders; don't send them again after upgrade
	for key in (BIRTHDAY_REMINDERS_LAST_SENT_KEY, WORK_ANNIVERSARY_REMINDERS_LAST_SENT_KEY):
		frappe.db.set_default(key, nowdate())
