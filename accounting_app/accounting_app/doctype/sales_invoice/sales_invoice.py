# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime

class SalesInvoice(Document):
	def on_submit(self):
		self.invoice_number = random.randint(100, 10000)
		amount = 0
		exists = frappe.db.exists(
			"Sales Invoice",
			{
			"invoice_number": self.invoice_number
			}
		)

		if exists:
			frappe.throw("Something went wrong with the invoice number, please try again")
		for each_item in self.items_details:
			amount = each_item.price + amount
		self.amount = amount
		self.date = datetime.now()

		""" Entering value for payment entry for customer """

		payment_entry_for_customer = frappe.new_doc('Payment Entry For Customer')
		payment_entry_for_customer.customer_name = self.supplier_name
		payment_entry_for_customer.paid_to_account = self.assets_account_number
		payment_entry_for_customer.account_details = self.debit_from_account
		payment_entry_for_customer.payment_mode = self.payment_mode
		payment_entry_for_customer.date_of_payment = self.date
		payment_entry_for_customer.amount = self.amount
		payment_entry_for_customer.invoice_number = self.invoice_number
		payment_entry_for_customer.transaction = str(uuid.uuid1())
		payment_entry_for_customer.save()
		payment_entry_for_customer.submit()

		""" Entering values in the Journal for customer"""

		journal_entry = frappe.new_doc('Journal Entry')
		account_entry = frappe.new_doc('Account Entries')
		account_entry.update({
			'account': self.assets_account_number,
			'party': self.supplier_name,
			'party_type': "Customer",
			"debit": 0.00,
			"credit": self.amount
		})

		# journal_entry.entries.append(account_entry)
		journal_entry.total_credit = self.amount
		journal_entry.total_debit = 0.00

		journal_entry.save()
		journal_entry.submit()

		""" Saving data/ entry for purchase in general ledger"""
		general_ledger = frappe.new_doc('General Ledger')
		general_ledger.transaction_date = self.date
		general_ledger.account = self.assets_account_number
		general_ledger.against_account = self.debit_from_account
		general_ledger.voucher_type = "Sales Invoice"
		general_ledger.debit = 0.00
		general_ledger.credit = self.amount
		general_ledger.created_at = datetime.now()

		general_ledger.save()
		general_ledger.submit()
