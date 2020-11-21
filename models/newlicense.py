#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime
from odoo.addons.ehcs_qr_code_base.models.qr_code_base import generate_qr_code


class res_users(models.Model):
    _inherit = 'res.users'

    section = fields.Many2one('nia.section', 'section')
    technical_authority = fields.Many2one('technical.authority', '')
    

class technical_authority(models.Model):
    _name = 'technical.authority'

    name = fields.Char('')


class nia_fees(models.Model):
    _name = 'nia.fees'

    name = fields.Char('')
    amount = fields.Char('')


class nia_section(models.Model):
    _name = 'nia.section'

    name = fields.Char('')
    seq = fields.Integer('',default=1)
    


class child_activity(models.Model):
    _name = 'child.activity'

    name = fields.Char('')
    parnet_activity = fields.Many2one('parnet.activity', 'parnet activity')
    



class parnet_activity(models.Model):
    _name = 'parnet.activity'

    name = fields.Char('')

class general_secretary(models.Model):
    _name = 'general.secretary'

    name = fields.Char('')    

class nia_new_license(models.Model):
    _name = 'nia.new_license'



    company_id = fields.Many2one(
        string='Company', 
        comodel_name='res.company', 
        required=True, 
        default=lambda self: self.env.user.company_id
    )

    
    state = fields.Selection([('1', 'draft'),('2', 'payment'),('3', 'technical authority'),('4', 'payment'),('5', 'Business Names Registrar'),('6', 'payment'),('7', 'section'),('8', 'section manager'),('9', 'General manager'),('10', 'General Secretary'),('11', 'Delivery'),('12', 'profile'),('13', 'Done'),('reject', 'rejected')],string='state',default='1')
    order_number = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('increment_profile'))
    name = fields.Char(string='Order by')
    project = fields.Char(string='')
    representative  = fields.Selection([('1', 'Owner'), ('2', 'delegate'),('3', 'assignment')],'representative')
    address = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    id_type = fields.Char()
    id_number = fields.Char()
    issuance_date = fields.Date()
    date_now = fields.Date('',default=fields.Date.today)
    Legal_form = fields.Selection([('person', 'person'),('company', 'company'),('partnership', 'partnership')],)
    fees = fields.Many2one('nia.fees', 'fees')
    

    company_name = fields.Char()
    section = fields.Many2one('nia.section', 'section')
    technical_authority = fields.Many2one('technical.authority', 'technical authority')
    respansiable = fields.Many2one('res.users', 'respansiable')
    parnet_activites = fields.Many2one('parnet.activity', 'parnet activites')
    child_activites = fields.Many2one('child.activity', 'child activites')
    activity_description = fields.Char()
    proposed_site = fields.Char()    
    space_required = fields.Char()
    project_capital = fields.Char()    
    capital_payback_period = fields.Char()
    main_products = fields.Text()
    child_products = fields.Text()
    foreign_participation = fields.Char()
    employment_count = fields.Char()
    local_employment = fields.Char()
    foreign_employment = fields.Char()
    owners = fields.One2many('nia.owners','new_license','owners')
    license_yaer =  fields.Integer(default=fields.Datetime.now().year)
    license_number = fields.Char('',compute='get_license_number')
    license_date = fields.Date('',default=fields.Date.today)
    business_name = fields.Char('')
    business_name_number = fields.Char('')
    technical_authority_comment = fields.Html('')
    section_comment = fields.Html('')
    section_manager_comment = fields.Html('')
    general_manager_comment = fields.Html('')
    general_secretary_comment = fields.Html('')
    attachments = fields.One2many('request.attachmens','nia_new_license','attachments')


    features = fields.Html('')
    terms = fields.Html('')
    note = fields.Html('')
    cc = fields.Html('')
    general_secretary = fields.Many2one('general.secretary', '')
    
    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')
    

    @api.onchange('section')
    def ganti_domain(self):
        
        return {
            'domain':
                {
                    'respansiable': [('section', '=', self.section.id)]
                },
        }
    
 
    
    def _generate_qr_code(self):
        qr_code = self.business_name_number
        self.qr_image = generate_qr_code(qr_code)      

    def print_payment(self):
       # data['form'].update(self.read(['date_from','date_to','report_type','request_type','project','name','date_now','section'])[0])  
        return self.env.ref('new_license_request.print_payment_doc').report_action(self)    
    
    def print_license(self):
       # data['form'].update(self.read(['date_from','date_to','report_type','request_type','project','name','date_now','section'])[0])  
        return self.env.ref('new_license_request.print_new_license').report_action(self)       


    #@api.onchange('section')
    def get_license_number(self):
        for rec in self:
            section = self.env['nia.section'].search([('id','=',self.section.id)])
            num = section.seq
            #print ('*******************   num           *******************',num)
            rec.license_number = str(num)+'/'+rec.section.name+'/'+str(rec.license_yaer)
            #print ('*******************section seq *******************',section.seq)
            return rec.license_number
            next_year = rec.license_yaer+1
            if rec.license_yaer != next_year:
                section.seq = section.seq +1
            else:
                section.seq = 1
    
    def data_confirm(self):
        for doc in self:
            
            doc.state = '2'      
    def pay1(self):
        for doc in self:
            doc.state = '3'

    def technical_authority_confirm(self):
        for doc in self:
            doc.state = '4'


    def technical_authority_reject(self):
        for doc in self:
            doc.state = 'reject'



    def pay2(self):
        for doc in self:
            doc.state = '5'

    def Business_Names_Registrar(self):
        for doc in self:
            doc.state = '6'


    def pay3(self):
        for doc in self:
            doc.state = '7'

    def section_confirm(self):
        for doc in self:
            doc.state = '8'

    def section_manager_confirm(self):
        for doc in self:
            doc.state = '9'

    def section_manager_reject(self):
        for doc in self:
            doc.state = '7'


    def general_manager_confirm(self):
        for doc in self:
            doc.state = '10'

    def general_manager_reject(self):
        for doc in self:
            doc.state = '7'

    def general_secretary_confirm(self):
        for doc in self:
            doc.state = '11'

    def general_secretary_reject(self):
        for doc in self:
            doc.state = '9'

    def delivery(self):
        for doc in self:
            doc.state = '12'

    def create_profile(self):
        for doc in self:
            
            profile = self.env['res.partner']
            vals = {
                'name': self.project,
                'parnet_activites': self.parnet_activites.id,
                'employment_count': self.employment_count,
                'local_employment': self.local_employment,
                'foreign_employment': self.foreign_employment,
                'activity_description' : self.activity_description,
                'project_capital' : self.project_capital,
                'section' : self.section.id,
                'license_number' : self.license_number,                
                'child_activites' : self.child_activites.id,
                #'owners' : [4,self.owners.id],
                #'docs': [4,self.attachments.id],
                'license_yaer': self.license_yaer,
                'license_date': self.license_date,
                'phone' : self.phone,
                'mobile' : self.mobile,
                'email' : self.email,
                'company_type' : self.Legal_form,
                'parent_id' : self.company_id.partner_id.id,
                'business_name' : self.business_name

                
            }
            
            new_profile = profile.create(vals)
            if  new_profile:
                for rec in self.attachments:
                    self.ensure_one()
                    new_profile.docs = ([(4,rec.id)])
                for rec in self.owners:
                    self.ensure_one()
                    new_profile.owners = ([(4,rec.id)])
                print("********************************new profile***********************",new_profile)
            doc.state = '13'

class nia_owners(models.Model):
    _name = 'nia.owners'

    name = fields.Char()
    contribution_ratio = fields.Char('')
    shares_number = fields.Char('')
    amount = fields.Char('')
    nationality = fields.Many2one('nia.nationality','nationality')    
    representative  = fields.Selection([('1', 'Owner'), ('2', 'agent'),('3', 'contributor')],'representative')
    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    id_type = fields.Char()
    id_number = fields.Char()
    new_license = fields.Many2one('nia.new_license', 'new_license')
    profile = fields.Many2one('res.partner', 'profile')
    

    

class nia_nationality(models.Model):
    _name = 'nia.nationality'


    name = fields.Char('country')

    
    
        
    
    
    
    
    


