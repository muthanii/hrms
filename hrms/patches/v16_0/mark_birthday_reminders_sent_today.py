import frappe
from frappe.utils import nowdate

from hrms.controllers.employee_reminders import BIRTHDAY_REMINDERS_LAST_SENT_KEY


def execute():
	# the old daily job has already sent today's reminders; don't send them again after upgrade
	frappe.db.set_default(BIRTHDAY_REMINDERS_LAST_SENT_KEY, nowdate())
