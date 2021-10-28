from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale



class OpenHouse(http.Controller):

    # @http.route('/customer_webform', type="http", auth="public", website=True)
    # def customer_webform(self, **kw):
    #     print("Execution Here.........................")
    #     return http.request.render('final_project.create_customer', {'trader': 'Odoo Mates Test 123'
    #                                                                   })

    # @http.route('/create/webcustomer', type="http", auth="public", website=True)
    # def create_webcustomer(self, **kw):
    #     print("Data Received.....", kw)
    #     request.env['customer.estate'].sudo().create(kw)
    #     return request.render("final_project.customer_thanks", {})

    # @http.route('/create/webcustomer', type="http", auth="public", website=True)
    # def create_webcustomer(self, **kw):
    #     http.request.env['res.users'].sudo().create({
    #         'name': 'testa',
    #         'login': 'testa',
    #     })
    #     return request.render("final_project.customer_thanks", {})

    # Fetching Data
    @http.route('/warehouse_webform', website=True, auth='user')
    def hospital_patient(self, **kw):
        # return "Thanks for watching"
        patients = request.env['real.estate'].sudo().search([])
        productvalue_list = []
        for app in patients:
            vals = {
              'name':  app.name,               
              'expected_price': app.expected_price,
              'status': app.status,
              'property_image': app.property_image,
            }
            productvalue_list.append(vals)
        print("ProductDeatils", productvalue_list)
        # return {
            
        #     'productvalue_list': productvalue_list,
        # }
        return request.render("final_project.warehouse_list", {
            'patients': patients,
            'productvalue_list': productvalue_list
        })






    # @http.route('/patient_webform', website=True, auth='user')
    # def patient_webform(self):
    #     return request.render("om_hospital.patient_webform", {})
    #
    # # Check and insert values from the form on the model <model>
    # @http.route(['/create_web_patient'], type='http', auth="public", website=True)
    # def patient_contact_create(self, **kwargs):
    #     print("ccccccccccccc")
    #     request.env['hospital.patient'].sudo().create(kwargs)
    #     return request.render("om_hospital.patient_thanks", {})



    # Sample Controller Created
    # @http.route('/hospital/patient/', website=True, auth='user')
    # def hospital_patient(self, **kw):
    #     # return "Thanks for watching"
    #     patients = request.env['hospital.patient'].sudo().search([])
    #     return request.render("om_hospital.patients_page", {
    #         'patients': patients
    #     })

    # # Sample Controller Created
    # @http.route('/update_patient', type='json', auth='user')
    # def update_patient(self, **rec):
    #     if request.jsonrequest:
    #         if rec['id']:
    #             print("rec...", rec)
    #             patient = request.env['hospital.patient'].sudo().search([('id', '=', rec['id'])])
    #             if patient:
    #                 patient.sudo().write(rec)
    #             args = {'success': True, 'message': 'Patient Updated'}
    #     return args

    # @http.route('/create_patient', type='json', auth='user')
    # def create_patient(self, **rec):
    #     if request.jsonrequest:
    #         print("rec", rec)
    #         if rec['name']:
    #             vals = {
    #                 'patient_name': rec['name'],
    #                 'email_id': rec['email_id']
    #             }
    #             new_patient = request.env['hospital.patient'].sudo().create(vals)
    #             print("New Patient Is", new_patient)
    #             args = {'success': True, 'message': 'Success', 'id': new_patient.id}
    #     return args

    # @http.route('/get_patients', type='json', auth='user')
    # def get_patients(self):
    #     print("Yes here entered")
    #     patients_rec = request.env['hospital.patient'].search([])
    #     patients = []
    #     for rec in patients_rec:
    #         vals = {
    #             'id': rec.id,
    #             'name': rec.patient_name,
    #             'sequence': rec.name_seq,
    #         }
    #         patients.append(vals)
    #     print("Patient List--->", patients)
    #     data = {'status': 200, 'response': patients, 'message': 'Done All Patients Returned'}
    #     return data