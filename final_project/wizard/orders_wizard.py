from datetime import timedelta
from odoo import models, fields, api


class orderList(models.TransientModel):
    _name = 'order.list.wizard'
    _description = 'Order Details'
   

    
    oname = fields.Char(string='Order Details')
    customer_ids = fields.Many2many('customer.estate', string='Related Customer')
    property_ids = fields.Many2one('real.estate', string='Related Property')

    

    
    def action_print_report(self):
        print("test..", self.read()[0])
        data = {
            
            'customer_ids': self.customer_ids.ids,
            'property_ids': self.property_ids.id,
            # 'model': 'order.list.wizard',
            'form': self.read()[0],
        }
        
        return self.env.ref('final_project.action_report_ordered_property').report_action(self, data=data)