from datetime import timedelta
from odoo import models, fields, api


class orderList(models.TransientModel):
    _name = 'order.list.wizard'
    _description = 'Order Details'
   

    
    oname = fields.Char(string='Order Details')
    # ordered_product = fields.Many2many('product.list', string='Available Products')
    customer_ids = fields.Many2many('customer.estate', string='Related Customer')
    property_ids = fields.Many2many('real.estate', string='Related Property')

    

    
    def action_print_report(self):
        data = {}
        # report_obj = self.env.ref("final_project.action_report_ordered_property")
        # return report_obj.report_action(self, data={"fecha_inicio": self.fecha_inicio, "fecha_fin": self.fecha_fin})
        return self.env.ref('final_project.action_report_ordered_property').report_action(self, data=data)