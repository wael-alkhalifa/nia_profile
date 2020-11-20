#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
 

class decisions(models.Model):
     _name = 'decisions.decisions'
     _inherit = ['mail.thread']
     _description = 'decisions'
     daft_check = fields.Boolean('',default=True)
     
     request_type = fields.Selection([('1', 'rental form'),('2', 'needs statement'),('3', 'license renewal'),('4', ' typical privileges'),('5', 'shapeliness request'),('6', 'transportation recommendation'),('7', 'model exception'),('8', ' resumption request'),('9', 'modify decision'),('10', 'renewal decision'),('11', 'change activity'), ('12', 'conduct request'),('13', 'mortgage_request'),('14', ' enter partner'),('15', 'breakup partnership'),('16', 'change businessname'),('17', 'transfer_ownership'),('18', ' reissued request'),('19', 'cancel license')],string='request type')
     fees = fields.Many2one('nia.fees', 'fees')
     receipt = fields.Char('')
     

     rental_form = fields.Selection([('1', 'draft'),('2', 'payment'),('3','technical authority'),('4', 'technical authority'),('5', 'sections'),('6','field_visit_need'),('7', 'Follow-up and evaluation'),('8', 'sections'),('9', 'section manager'),('10', ' general_manager'),('11', 'Legal advisor'),('12', ' general_manager'),('13', ' section manager'),('14', 'sections'),('15', ' section manager'),('16', 'general manager'),('17','General Secretary'),('18', 'payment'),('19','Delivery'),('20','reject'),('21', 'profile update'),('22', 'done')],'',default='1', track_visibility='onchange')
     needs_statements = fields.Selection([('1', 'draft'),('2', 'payment'),('3', 'technical authority'),('4', 'sections'),('5', 'section manager'),('6', 'Customs'),('7', 'profile update'),('8', 'done')],'',default='1')
     license_renewal = fields.Selection([('1', 'draft'),('2', 'payment'),('3','technical authority'),('4', 'technical authority'),('5', 'sections'),('6', 'section manager'),('7','conflict'),('8', 'Legal advisor'),('9', 'section manager'),('10', 'Business Names Registrar'),('11', ' section manager'),('12', ' sections'),('13', ' section manager'),('14', 'general manager'),('15','General Secretary'),('16', 'payment'),('17','Delivery'),('18','reject'),('19', 'profile update'),('20', 'done')],'',default='1', track_visibility='onchange')
     model_exception = fields.Selection([('1', 'draft'),('2', 'payment'),('3', 'general manager'),('4', 'General Secretary'),('5', 'Customs'),('6', 'profile'), ('7' ,'Done'),('10', 'reject')],'',default='1')
     resumption_request = fields.Selection([('1', 'draft'),('2','General Secretary'),('3', 'general manager'),('4', 'section manager'),('5', 'sections'),('6', 'General Secretary'),('7', 'Delivery'),('8', 'profile update'),('9', 'Done')],'',default='1')
     modify_decision = fields.Selection([('1', 'draft'),('2', 'payment'),('3','technical authority'),('4', 'technical authority'),('8', 'sections'),('9', 'section manager'),('10', ' general_manager'),('13', ' section manager'),('14', 'sections'),('15', ' section manager'),('16', 'general manager'),('17','General Secretary'),('18', 'payment'),('19','Delivery'),('20','reject'),('21', 'profile update'),('22', 'done')],'',default='1', track_visibility='onchange')
     change_activity = fields.Selection([('1', 'draft'),('2', 'payment'),('3','technical authority'),('4', 'technical authority'),('5', 'sections'),('6','field_visit_need'),('7', 'Follow-up and evaluation'),('8', 'sections'),('9', 'section manager'),('10', ' general_manager'),('13', ' section manager'),('14', 'sections'),('15', ' section manager'),('16', 'general manager'),('17','General Secretary'),('18', 'payment'),('19','Delivery'),('20','reject'),('21', 'profile update'),('22', 'done')],'',default='1', track_visibility='onchange')
     enter_partner = fields.Selection([('1', 'draft'),('2', 'payment'),('3','technical authority'),('4', 'technical authority'),('5', 'sections'),('6','field_visit_need'),('7', 'Follow-up and evaluation'),('8', 'sections'),('9', 'section manager'),('10', ' general_manager'),('11', 'Legal advisor'),('12', ' general_manager'),('13', ' section manager'),('14', 'sections'),('14a', 'Business Names Registrar'),('14b', 'sections'),('15', ' section manager'),('16', 'general manager'),('17','General Secretary'),('18', 'payment'),('19','Delivery'),('20','reject'),('21', 'profile update'),('22', 'done')],'',default='1', track_visibility='onchange')
     cancel_license = fields.Selection([('1', 'draft'),('2', 'sections'),('3', 'section manager'),('5', 'commercial registrar'),('6', 'sections'),('7', ' section manager'),('8', 'general manager'),('9','General Secretary'),('10','Delivery'),('11','reject'),('12', 'profile update'),('13', 'done')],'',default='1', track_visibility='onchange')
     project_id = fields.Many2one('res.partner', 'project')
     company_id = fields.Many2one(
        string='Company', 
        comodel_name='res.company', 
        required=True, 
        default=lambda self: self.env.user.company_id
     )     
     project = fields.Char(string='project')
     name = fields.Char(string='Order by')
     employee = new_field = fields.Many2one('res.users','employee',default=lambda self: self.env.user.id)     
     order_number = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
     order_date =  fields.Date(default=fields.Date.today)
     section = fields.Many2one('nia.section', 'section',related='project_id.section')
     attachments = fields.One2many('request.attachmens','decisions','', track_visibility='onchange')   
     note = fields.Html('', track_visibility='onchange')
     technical_authority_comment = fields.Html('', track_visibility='onchange')
     legal_advisor_comment = fields.Html('', track_visibility='onchange')
     business_name_registrar_comment = fields.Html('', track_visibility='onchange')
     section_comment = fields.Html('', track_visibility='onchange')
     section_manager_comment = fields.Html('', track_visibility='onchange')
     general_manager_comment = fields.Html('', track_visibility='onchange')
     general_secretary_comment = fields.Html('', track_visibility='onchange')
  
     business_name = fields.Char(string='Business name',related='project_id.business_name')
     phone = fields.Char(string='phone')
     rental_site = fields.Char(string='rental site')
     land_number = fields.Char(string='land number')
     square = fields.Char(string='square')
     area = fields.Char(string='area')
     activity_description = fields.Char(string='',related='project_id.activity_description')
     license_number = fields.Char(string='license number',related='project_id.license_number')
     license_date = fields.Date(string='license date',related='project_id.license_date')
     rent_reasons  = fields.Char(string='rent reasons')
     steps = fields.Text(string='steps')
     date_now = fields.Date('',default=fields.Date.today)
     field_visit = fields.Many2one('field.visit', 'field_visit', track_visibility='onchange')
     

     def create_visit(self):
        for doc in self:
            
            field_visit = self.env['field.visit'].search([('project_id','=',self.project_id.id)])
            vals = {
                'project_id': self.project_id.id,
                'visit_type': '3',
                'section': self.section.id,
                'company_id': self.company_id.id

                
            }
            
            new_field_visit = field_visit.create(vals)
            if  new_field_visit:
                 self.field_visit = new_field_visit
                 print("******************************** new_field_visit***********************",new_field_visit)
            doc.state = '13'

     
     def print_payment(self):
        return self.env.ref('decisions.decisions_payment_doc').report_action(self) 

     def update_profile(self):
          profile = self.env['res.partner'].search([('id','=',self.project_id.id)])
          for rec in profile:
               rec.decision_details = [(4,self.id)]
               print ('*******************   decision_details           *******************',rec.decision_details)


     def daft_check_confirm(self):
          for rec in self:
               if rec.request_type == '1':
                    rec.rental_form = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '13':
                    rec.rental_form = '2'
                    self.daft_check = False
                    break

               if rec.request_type == '2':
                    rec.needs_statements = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '3':
                    rec.license_renewal = '2'
                    self.daft_check = False
                    break 
               if rec.request_type == '19':
                    rec.license_renewal = '2'
                    self.daft_check = False
                    break 
               if rec.request_type == '7':
                    rec.model_exception = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '8':
                    rec.change_activity = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '9':
                    rec.modify_decision = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '10':
                    rec.modify_decision = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '4':
                    rec.modify_decision = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '5':
                    rec.modify_decision = '2'
                    self.daft_check = False
                    break


               if rec.request_type == '6':
                    rec.change_activity = '2'
                    self.daft_check = False
                    break
               if rec.request_type == '11':
                    rec.change_activity = '2'
                    self.daft_check = False
                    break

               if rec.request_type == '12':
                    rec.modify_decision = '2'
                    self.daft_check = False
                    break

               if rec.request_type == '18':
                    rec.change_activity = '2'
                    self.daft_check = False
                    break


               if rec.request_type == '14':
                    rec.enter_partner = '2'
                    self.daft_check = False
                    break


               if rec.request_type == '15':
                    rec.enter_partner = '2'
                    self.daft_check = False
                    break

               if rec.request_type == '16':
                    rec.enter_partner = '2'
                    self.daft_check = False
                    break

               if rec.request_type == '17':
                    rec.enter_partner = '2'
                    self.daft_check = False
                    break


          self.daft_check = True


     def enter_partner_confirm(self):
          for doc in self:
              if doc.enter_partner == '2':
                   doc.enter_partner = '5'
                   break
              if doc.enter_partner == '3':
                   doc.enter_partner = '4'
                   break
              if doc.enter_partner == '4':
                   doc.enter_partner = '5'
                   break     
              if doc.enter_partner == '5':
                   doc.enter_partner = '6'
                   break 
              if doc.enter_partner == '6':
                   doc.enter_partner = '7'
                   break
              if doc.enter_partner == '7':
                   self.create_visit()
                   doc.enter_partner = '8'
                   break     
              if doc.enter_partner == '8':
                   doc.enter_partner = '9'
                   break
              if doc.enter_partner == '9':
                   doc.enter_partner = '10'
                   break 
              if doc.enter_partner == '10':
                   doc.enter_partner = '11'
                   break 
              if doc.enter_partner == '11':
                   doc.enter_partner = '12'
                   break 

              if doc.enter_partner == '12':
                   doc.enter_partner = '13'
                   break
              if doc.enter_partner == '13':
                   doc.enter_partner = '14'
                   break
              if doc.enter_partner == '14':
                   doc.enter_partner = '14a'
                   break  
              if doc.enter_partner == '14a':
                   doc.enter_partner = '14b'
                   break 

              if doc.enter_partner == '14b':
                   doc.enter_partner = '15'
                   break    
              if doc.enter_partner == '15':
                   doc.enter_partner = '16'
                   break 
              if doc.enter_partner == '16':
                   doc.enter_partner = '17'
                   break
              if doc.enter_partner == '17':
                   doc.enter_partner = '18'
                   break     
              if doc.enter_partner == '18':
                   doc.enter_partner = '19'
                   break
              if doc.enter_partner == '19':
                   doc.enter_partner = '21'
                   break 
              if doc.enter_partner == '21':
                   self.update_profile()
                   doc.enter_partner = '21'


     def enter_partner_reject(self):
          for doc in self:
              if doc.enter_partner == '3':
                   doc.enter_partner = '5'
                   break 

              if doc.enter_partner == '6':
                   doc.enter_partner = '8'
                   break 
              if doc.enter_partner == '14b':
                   doc.enter_partner = '20'
                   break 
              if doc.enter_partner == '20':
                   self.update_profile()
                   break 
              if doc.enter_partner == '17':
                   doc.enter_partner = '16'
                   break  
              if doc.enter_partner == '16':
                   doc.enter_partner = '15'
                   break 
              if doc.enter_partner == '15':
                   doc.enter_partner = '14'
                   break  
 
 


     def change_activity_confirm(self):
          for doc in self:
              if doc.change_activity == '2':
                   doc.change_activity = '3'
                   break
              if doc.change_activity == '3':
                   doc.change_activity = '4'
                   break
              if doc.change_activity == '4':
                   doc.change_activity = '5'
                   break     
              if doc.change_activity == '5':
                   doc.change_activity = '6'
                   break 
              if doc.change_activity == '6':
                   doc.change_activity = '7'
                   break
              if doc.change_activity == '7':
                   self.create_visit()
                   doc.change_activity = '8'
                   break     
              if doc.change_activity == '8':
                   doc.change_activity = '9'
                   break
              if doc.change_activity == '9':
                   doc.change_activity = '10'
                   break 
              if doc.change_activity == '10':
                   doc.change_activity = '13'
                   break 


              if doc.change_activity == '13':
                   doc.change_activity = '14'
                   break
              if doc.change_activity == '14':
                   doc.change_activity = '15'
                   break     
              if doc.change_activity == '15':
                   doc.change_activity = '16'
                   break 
              if doc.change_activity == '16':
                   doc.change_activity = '17'
                   break
              if doc.change_activity == '17':
                   doc.change_activity = '18'
                   break     
              if doc.change_activity == '18':
                   doc.change_activity = '19'
                   break
              if doc.change_activity == '19':
                   doc.change_activity = '21'
                   break 
              if doc.change_activity == '21':
                   self.update_profile()
                   doc.change_activity = '21'



     def change_activity_reject(self):
          for doc in self:
              if doc.change_activity == '3':
                   doc.change_activity = '5'
                   break 

              if doc.change_activity == '6':
                   doc.change_activity = '8'
                   break 
              if doc.change_activity == '14':
                   doc.change_activity = '20'
                   break 
              if doc.change_activity == '20':
                   self.update_profile()
                   break 
              if doc.change_activity == '17':
                   doc.change_activity = '16'
                   break  
              if doc.change_activity == '16':
                   doc.change_activity = '15'
                   break 
              if doc.change_activity == '15':
                   doc.change_activity = '14'
                   break  

 





     def modify_decision_confirm(self):

          for doc in self:

              if doc.modify_decision == '2':
                   doc.modify_decision = '3'
                   break
              if doc.modify_decision == '3':
                   doc.modify_decision = '4'
                   break
              if doc.modify_decision == '4':
                   doc.modify_decision = '8'
                   break        
              if doc.modify_decision == '8':
                   doc.modify_decision = '9'
                   break
              if doc.modify_decision == '9':
                   doc.modify_decision = '10'
                   break 
              if doc.modify_decision == '10':
                   doc.modify_decision = '13'
                   break 


              if doc.modify_decision == '13':
                   doc.modify_decision = '14'
                   break
              if doc.modify_decision == '14':
                   doc.modify_decision = '15'
                   break     
              if doc.modify_decision == '15':
                   doc.modify_decision = '16'
                   break 
              if doc.modify_decision == '16':
                   doc.modify_decision = '17'
                   break
              if doc.modify_decision == '17':
                   doc.modify_decision = '18'
                   break     
              if doc.modify_decision == '18':
                   doc.modify_decision = '19'
                   break
              if doc.modify_decision == '19':
                   doc.modify_decision = '21'
                   break 
              if doc.modify_decision == '21':
                   self.update_profile()
                   doc.modify_decision = '21'

                



     def modify_decision_reject(self):
          for doc in self:
              if doc.modify_decision == '3':
                   doc.modify_decision = '8'
                   break 

              if doc.modify_decision == '14':
                   doc.modify_decision = '20'
                   break 
              if doc.modify_decision == '20':
                   self.update_profile()
                   break 
              if doc.modify_decision == '17':
                   doc.modify_decision = '16'
                   break  
              if doc.modify_decision == '16':
                   doc.modify_decision = '15'
                   break 
              if doc.modify_decision == '15':
                   doc.modify_decision = '14'
                   break 





     def rental_confirm(self):

          for doc in self:

              if doc.rental_form == '2':
                   doc.rental_form = '3'
                   break
              if doc.rental_form == '3':
                   doc.rental_form = '4'
                   break
              if doc.rental_form == '4':
                   doc.rental_form = '5'
                   break     
              if doc.rental_form == '5':
                   doc.rental_form = '6'
                   break 
              if doc.rental_form == '6':
                   doc.rental_form = '7'
                   break
              if doc.rental_form == '7':
                   self.create_visit()
                   doc.rental_form = '8'
                   break     
              if doc.rental_form == '8':
                   doc.rental_form = '9'
                   break
              if doc.rental_form == '9':
                   doc.rental_form = '10'
                   break 
              if doc.rental_form == '10':
                   doc.rental_form = '11'
                   break 
              if doc.rental_form == '11':
                   doc.rental_form = '12'
                   break 

              if doc.rental_form == '12':
                   doc.rental_form = '13'
                   break
              if doc.rental_form == '13':
                   doc.rental_form = '14'
                   break
              if doc.rental_form == '14':
                   doc.rental_form = '15'
                   break     
              if doc.rental_form == '15':
                   doc.rental_form = '16'
                   break 
              if doc.rental_form == '16':
                   doc.rental_form = '17'
                   break
              if doc.rental_form == '17':
                   doc.rental_form = '18'
                   break     
              if doc.rental_form == '18':
                   doc.rental_form = '19'
                   break
              if doc.rental_form == '19':
                   doc.rental_form = '21'
                   break 
              if doc.rental_form == '21':
                   self.update_profile()
                   doc.rental_form = '21'
                



     def rental_reject(self):
          for doc in self:
              if doc.rental_form == '3':
                   doc.rental_form = '5'
                   break 

              if doc.rental_form == '6':
                   doc.rental_form = '8'
                   break 
              if doc.rental_form == '14':
                   doc.rental_form = '20'
                   break 
              if doc.rental_form == '20':
                   self.update_profile()
                   break 
              if doc.rental_form == '17':
                   doc.rental_form = '16'
                   break  
              if doc.rental_form == '16':
                   doc.rental_form = '15'
                   break 
              if doc.rental_form == '15':
                   doc.rental_form = '14'
                   break    


     def model_exception_confirm(self):
          for doc in self:
              if doc.model_exception == '2':
                   doc.model_exception = '3'
                   break
              if doc.model_exception == '3':
                   doc.model_exception = '4'
                   break
              if doc.model_exception == '4':
                   doc.model_exception = '5'
                   break     
              if doc.model_exception == '5':
                   self.update_profile()
                   doc.model_exception = '6'
                   break 
              if doc.model_exception == '6':
                   self.update_profile()
                   doc.model_exception = '7'
                   break 
              if doc.model_exception == '10':
                   self.update_profile()
                   break 
     def model_exception_reject(self):
          for doc in self:
              if doc.model_exception == '4':
                   doc.model_exception = '10'
                   break 

     def resumption_request_confirm(self):
          for doc in self:

              if doc.resumption_request == '2':
                   doc.resumption_request = '3'
                   break
              if doc.resumption_request == '3':
                   doc.resumption_request = '4'
                   break
              if doc.resumption_request == '4':
                   doc.resumption_request = '5'
                   break     
              if doc.resumption_request == '5':
                   doc.resumption_request = '6'
                   break 
              if doc.resumption_request == '6':
                   doc.resumption_request = '7'
                   break
              if doc.resumption_request == '7':
                   doc.resumption_request = '8'
                   break
              if doc.resumption_request == '8':
                   self.update_profile()
                   doc.resumption_request = '9'
                   break

     def needs_statements_confirm(self):
          for doc in self:

              if doc.needs_statements == '2':
                   doc.needs_statements = '3'
                   break
              if doc.needs_statements == '3':
                   doc.needs_statements = '4'
                   break
              if doc.needs_statements == '4':
                   doc.needs_statements = '5'
                   break 
              if doc.needs_statements == '5':
                   doc.needs_statements = '6'
                   break
              if doc.needs_statements == '6':
                   doc.needs_statements = '7'
                   break      
              if doc.needs_statements == '7':
                   self.update_profile()
                   doc.needs_statements = '8'
                   break 

     def needs_statements_reject(self):
          for doc in self:
              if doc.needs_statements == '5':
                   doc.needs_statements = '4'
                   break 



     def license_renewal_confirm(self):

          for doc in self:

              if doc.license_renewal == '2':
                   doc.license_renewal = '3'
                   break
              if doc.license_renewal == '3':
                   doc.license_renewal = '4'
                   break
              if doc.license_renewal == '4':
                   doc.license_renewal = '5'
                   break     
              if doc.license_renewal == '5':
                   doc.license_renewal = '6'
                   break 
              if doc.license_renewal == '6':
                   doc.license_renewal = '7'
                   break
              if doc.license_renewal == '7':
                   doc.license_renewal = '8'
                   break     
              if doc.license_renewal == '8':
                   doc.license_renewal = '10'
                   break
              if doc.license_renewal == '9':
                   doc.license_renewal = '10'
                   break 
              if doc.license_renewal == '10':
                   doc.license_renewal = '11'
                   break 
              if doc.license_renewal == '11':
                   doc.license_renewal = '12'
                   break 

              if doc.license_renewal == '12':
                   doc.license_renewal = '13'
                   break
              if doc.license_renewal == '13':
                   doc.license_renewal = '14'
                   break
              if doc.license_renewal == '14':
                   doc.license_renewal = '15'
                   break     
              if doc.license_renewal == '15':
                   doc.license_renewal = '16'
                   break 
              if doc.license_renewal == '16':
                   doc.license_renewal = '17'
                   break
              if doc.license_renewal == '17':
                   doc.license_renewal = '19'
                   break     
  
              if doc.license_renewal == '19':
                   self.update_profile()
                   doc.license_renewal = '20'

                



     def license_renewal_reject(self):
          for doc in self:
              if doc.license_renewal == '3':
                   doc.license_renewal = '5'
                   break 

              if doc.license_renewal == '7':
                   doc.license_renewal = '10'
                   break 
             # if doc.license_renewal == '12':
              #     doc.license_renewal = '18'
               #    break 
              if doc.license_renewal == '13':
                   doc.license_renewal = '12'
                   break 
              if doc.license_renewal == '14':
                   doc.license_renewal = '13'
                   break  
              if doc.license_renewal == '15':
                   doc.license_renewal = '14'
                   break 
              if doc.license_renewal == '18':
                   self.update_profile()
                   break  








































class request_attachmens(models.Model):
     _name = 'request.attachmens'
     _description = 'request attachmens'

     name = fields.Char(string='name')
     attachment = fields.Binary('attachment')
     profile = fields.Many2one('res.partner', 'profile',invisible=True)
     nia_new_license = fields.Many2one('nia.new_license', '')
     decisions = fields.Many2one('decisions.decisions', '')
     

     
     


   





