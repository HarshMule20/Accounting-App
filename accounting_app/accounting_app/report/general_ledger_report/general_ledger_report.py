# Copyright (c) 2013, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

def execute(filters=None):
	columns = [
		{
			"fieldname": "account",
			"fieldtype": "Data",
			"label": "Account"
		},
		{
			"fieldname": "transaction_date",
			"fieldtype": "Datetime",
			"label": "Transaction Date"
  		}
	]
	data = []
	return columns, data
