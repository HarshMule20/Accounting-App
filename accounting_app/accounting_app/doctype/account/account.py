# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.utils.nestedset import NestedSet
from random import randint
from datetime import datetime


class Account(NestedSet):
	nsm_parent_field = "parent_account"

	def before_submit(self):
		"""
			added a logic to generate random/unique number for account details
		"""

		n = 10
		range_start = 10**(n-1)
		range_end = (10**n)-1
		accountNumber = randint(range_start, range_end)
		self.account_number = accountNumber
		self.created_at = datetime.now()