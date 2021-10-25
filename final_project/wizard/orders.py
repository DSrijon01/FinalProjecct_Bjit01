from datetime import timedelta
from odoo import models, fields, api


class orderList(models.TransientModel):
    _name = 'order.list.wizard'
    _description = 'Order Details'
   

    
    oname = fields.Char(string='Order Details',required=True)
    # ordered_product = fields.Many2many('product.list', string='Available Products')
    customer_id = fields.Many2many('customer.estate', string='Related Customer')
    

    

    def action_print_report(self):
        
        data = {
            # 'model': 'order.list.wizard',
            # 'form': self.read()[0],
        }
        
        return self.env.ref('my_hotel.action_report_order_overview').report_action(self, data=data)