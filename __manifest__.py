{
    "name": "New Customer Module",
    "author": "Youcef Messelem",
    "license": "LGPL-3",
    "version": "17.0.1.0",
    "category": "Services",
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/customer_views.xml",
        "views/menu.xml",
    ],
    'installable': True,
    'application': True,
}