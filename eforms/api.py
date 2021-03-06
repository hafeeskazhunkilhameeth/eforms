import frappe

@frappe.whitelist()
def get_seen(dt, dn):
    df = frappe.db.get_value(dt, dn, "meta_seen")
    return df

@frappe.whitelist()
def set_seen(dt, dn):
    df = frappe.db.set_value(dt, dn, "meta_seen", "yes")
    return df

@frappe.whitelist()
def get_ticket_status(dt, dn):
    df = frappe.db.get_value(dt, dn, "status")
    return df