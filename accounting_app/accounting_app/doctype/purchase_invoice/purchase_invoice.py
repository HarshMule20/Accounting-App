# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random
import uuid
from datetime import datetime

class PurchaseInvoice(Document):
	def on_submit(self):
		self.invoice_number = random.randint(100, 10000)
		exists = frappe.db.exists(
			"Purchase Invoice",
			{
			"invoice_number": self.invoice_number
			}
		)

		if exists:
			frappe.throw("Something went wrong with the invoice number, please try again")

		amount = 0
		print("*****", self.item_details)
		for each_item in self.item_details:
			print("each data", each_item)
			amount = each_item.price + amount
		self.amount = amount
		self.date = datetime.now()

		""" Entering value for payment entry for supplier """
		
		payment_entry_for_supplier = frappe.new_doc('Payment Entry For Supplier')
		payment_entry_for_supplier.supplier_name = self.supplier_name
		payment_entry_for_supplier.paid_from_account = self.assets_account
		payment_entry_for_supplier.account_details = self.credit_account_number
		payment_entry_for_supplier.payment_mode = self.payment_mode
		payment_entry_for_supplier.date_of_payment = self.date
		payment_entry_for_supplier.amount = self.amount
		payment_entry_for_supplier.invoice_number = self.invoice_number
		payment_entry_for_supplier.transaction = str(uuid.uuid1())
		payment_entry_for_supplier.save()
		payment_entry_for_supplier.submit()

		""" Entering values in the Journal for supplier"""

		journal_entry = frappe.new_doc('Journal Entry')
		account_entry = frappe.new_doc('Account Entries')
		account_entry.update({
			'account': self.assets_account,
			'party': self.supplier_name,
			'party_type': "Supplier",
			"debit": self.amount,
			"credit": 0.00
		})

		# journal_entry.entries.append(account_entry)
		# journal_entry.entries = account_entry
		journal_entry.total_debit = self.amount
		journal_entry.total_credit = 0.00

		journal_entry.save()
		journal_entry.submit()

		""" Saving data/ entry for purchase in general ledger"""
		general_ledger = frappe.new_doc('General Ledger')
		general_ledger.transaction_date = self.date
		general_ledger.account = self.assets_account
		general_ledger.against_account = self.credit_account_number
		general_ledger.voucher_type = "Purchase Invoice"
		general_ledger.debit = self.amount
		general_ledger.credit = 0.00
		general_ledger.created_at = datetime.now()

		general_ledger.save()
		general_ledger.submit()