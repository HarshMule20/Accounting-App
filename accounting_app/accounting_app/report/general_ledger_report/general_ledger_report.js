// // Copyright (c) 2016, Harsh Mule and contributors
// // For license information, please see license.txt
// /* eslint-disable */

// frappe.query_reports["General Ledger Report"] = {
// 	"filters": [

// 	]
// };

// Copyright (c) 2016, Harsh Mule and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Ledger Report"] = {
	"filters": [
		{
			"fieldname": "transaction_date",
			"fieldtype": "Datetime",
			"in_list_view": 1,
			"label": "Transaction Date"
		   },
		   {
			"fieldname": "account",
			"fieldtype": "Data",
			"label": "Account"
		   },
		   {
			"fieldname": "fiscal_year",
			"fieldtype": "Data",
			"label": "Fiscal Year",
			"options": "Fiscal Year"
		   },
		   {
			"fieldname": "voucher_type",
			"default": "All",
			"fieldtype": "Select",
			"label": "Voucher type",
			"options": "Purchase Invoice\nSales Invoice\nPayment Entry For Supplier\nPayment Entry for Customer"
		   },
		   {
			"fieldname": "created_at",
			"fieldtype": "Date",
			"label": "Created At"
		   }
	]
};
