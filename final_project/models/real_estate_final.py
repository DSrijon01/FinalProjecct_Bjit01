# -*- coding: utf-8 -*-from custom_addons.real_estate.models.inheritance import restuser

from odoo import models, fields
from odoo import api 
from odoo.exceptions import ValidationError

class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Open House Property Management'
    

    ##Sql Constraints To validate the Price Fileds Input. 
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected price must be strictly positive'),
        ('check_surge_price', 'CHECK(surgeprice >= 0)', 'The selling price must be positive')
        
    ]



    


    name = fields.Char(string ='Title')
    active = fields.Boolean(default=True)
    description = fields.Char(string='Description')
    seller_signature = fields.Char(string='Seller Signature')
    pp_address = fields.Char(string="Address")
    expected_price = fields.Integer(string='Expected Price')
    avaiable_from = fields.Date(string='Available From')
    property_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    status = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('sold', 'Sold')],
        'State', default="draft")
    documents = fields.Binary(string='Documents', help ="Place Your Affiliated Documents Here")
    # model_viewer = fields.Binary(string="Model Viewer")    
    # pdocument_name = fields.Char(string ="File Name")

    rent_count = fields.Integer(compute="_compute_rent_count") 

    ##Basic Button Functionality 
    def make_draft(self):
        self.ensure_one()
        self.status = 'draft'   

    def make_available(self):
        self.ensure_one()
        self.status= 'available'
        

    def make_sold(self):
        self.ensure_one()
        self.status = 'sold'

    ##Printing Button Functionality 
    # @api.multi
    # def print_report(self):


    
    ## for computed field. 
    surgeprice = fields.Float(compute = "_compute_total", inverse ="_inverse_total", string = 'Future Price')
    
    ##database relationship
    ##many to many with the owners
    owner_bio =  fields.Many2many('real.owner',string='Owning')


    ##many 2 one view with owner
    # owner_info =  fields.Many2one('real.owner',string='Owning')
    
    # partner_id = fields.Many2one('res.partner',string="Partner")
    # newid = fields.Many2many('res.users', string="Working")
    
    ##Computed Field Logic. 
    @api.depends('expected_price')
    def _compute_total(self):
        for record in self:
            record.surgeprice = record.expected_price * 5 

    def _inverse_total(self):
        for record in self:
            record.surgeprice = record.expected_price - (record.expected_price * (10/100))

    ##For Name Constraints of the property.      
    @api.constrains('title')
    def check_title(self):
        for rec in self:
            error = self.env['real.estate'].search([('title', '=', rec.title)])
            if (error == rec.title):
                raise ValidationError(('Same Name'))
    

    

