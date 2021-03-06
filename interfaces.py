from zope.interface import Interface, Attribute

# Implementation - реализация
# Provide - обеспечить, **обслуживать**, оснащать.


class IAccountingEntry(Interface):
    cr=Attribute("Credit account")
    dr=Attribute("Debit account")
    amount=Attribute("Amount of money sent")
    currency=Attribute("A currency id")
    moment=Attribute("A DateTime moment of the entry")

class IDocument(Interface):
    def create():
        """
        Create document.
        """
    def delete():
        """
        Delete the document.
        """
    def save():
        """
        Store the document in a global storage,
        and create a set of accounting entries.
        """

class ICreditSlip(IDocument):
        def addentry(entry):
            """
            Adds an accounting
            entry in the credit slip.
            """

class IStorage(Interface):
    def store(document):
        """
        Store the document in storage
        """

