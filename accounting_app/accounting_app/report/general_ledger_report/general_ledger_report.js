// Copyright (c) 2016, Harsh Mule and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Ledger Report"] = {
	"filters": [
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
};
