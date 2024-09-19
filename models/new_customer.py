from odoo import api, fields, models


class NewCustomer(models.Model):
    _name = "new.customer"
    _inherit = ['mail.thread']
    _rec_name = 'full_name'
    _description = "New Customer Request From Salespersons"

    reference = fields.Char(string="Reference", default="New")
    full_name = fields.Char(string="Full Name", required=True, tracking=True)
    company_name = fields.Char(string="Company Name", required=True, tracking=True)
    mobile1 = fields.Char(string="Mobile 1", required=True, tracking=True)
    mobile2 = fields.Char(string="Mobile 2", required=False, tracking=True)
    area = fields.Selection([('ع', 'ع'), ('ص', 'ص'), ('م', 'م'), ('ف', 'ف'), ('د', 'د'), ('ت', 'ت')],
                            string="Area", required=True)
    year_of_last_matching = fields.Selection([
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
    ], string="Year of Last Matching", required=True)
    place = fields.Char(string="Place", required=True)
    customer_status = fields.Selection([
        ('new', 'زبون جديد'),
        ('old', 'زبون قديم')
    ], string="Customer Status", default="new", required=True)
    partner_id = fields.Many2one('res.partner', string="Old Name", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),

    ], default="draft", tracking=True)
    province = fields.Selection([
        ("بغداد", "بغداد"),
        ("البصرة", "البصرة"),
        ("نينوى", "نينوى"),
        ("أربيل", "أربيل"),
        ("السليمانية", "السليمانية"),
        ("دهوك", "دهوك"),
        ("كركوك", "كركوك"),
        ("النجف", "النجف"),
        ("كربلاء", "كربلاء"),
        ("بابل", "بابل"),
        ("ديالى", "ديالى"),
        ("الأنبار", "الأنبار"),
        ("المثنى", "المثنى"),
        ("ذي قار", "ذي قار"),
        ("ميسان", "ميسان"),
        ("واسط", "واسط"),
        ("القادسية", "القادسية"),
        ("صلاح الدين", "صلاح الدين")
    ],
        string="Province", default="بغداد"
    )
    address = fields.Text(string="Address")
    location = fields.Char(string="Google Map Link")
    image = fields.Image(string="Signboard")

    final_name = fields.Char(string="Full Customer Name", compute="_compute_name")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("reference") or vals["reference"] == "New":
                vals["reference"] = self.env['ir.sequence'].next_by_code('new.customer')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec['state'] = 'confirmed'

    def action_done(self):
        for rec in self:
            rec['state'] = 'done'

    def action_draft(self):
        for rec in self:
            rec['state'] = 'draft'

    def action_cancel(self):
        for rec in self:
            rec['state'] = 'canceled'

    def _compute_name(self):
        for rec in self:
            if rec['area'] == 'م':
                rec.final_name = rec['area'] + '-' + rec['company_name'] + '-' + rec['province'] + '-' \
                                 + rec['full_name'] + ' ( ' + rec['year_of_last_matching'] + ' )'
            else:
                rec.final_name = rec['area'] + '-' + rec['company_name'] + '-' + rec['place'] + '-' \
                                 + rec['full_name'] + ' ( ' + rec['year_of_last_matching'] + ' )'
