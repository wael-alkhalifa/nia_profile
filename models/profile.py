#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class nia_profile(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'


    is_projct = fields.Boolean(default='False')
    Legal_form = fields.Selection([('person', 'person'),('company', 'company'),('partnership', 'partnership')],)
    projct_number = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('increment_profile'))
    parnet_activites = fields.Many2one('parnet.activity', 'parnet activites')
    projct_nationality = fields.Selection([('1', 'national'), ('2', 'foreign'),('3', 'mixed')],'')
    employment_count = fields.Char()
    local_employment = fields.Char()
    foreign_employment = fields.Char()
    project_capital = fields.Char()
    tax_number = fields.Char()
    social_welfare_number = fields.Char()
    activity_description = fields.Char()
    place = fields.Char('')
    

    ###############################################
    license_id = fields.Many2one('nia.new_license','')
    license_number = fields.Char('')
    section = fields.Many2one('nia.section', 'section')
    license_yaer = fields.Integer('')
    license_date = fields.Date('')
    business_name = fields.Char(string='Business name')
    child_activites = fields.Many2one('child.activity', 'child activites')
    
    ####################################################################
       
    decision_number = fields.Char('')   
    decision_yaer = fields.Char('') 
    decision_address = fields.Selection([('1', 'rental form'),('2', 'needs statement'),('3', 'license renewal'),('4', ' typical privileges'),('5', 'shapeliness request'),('6', 'transportation recommendation'),('7', 'model exception'),('8', ' resumption request'),('9', 'modify decision'),('10', 'renewal decision'),('11', 'change activity'), ('12', 'conduct request'),('13', 'mortgage_request'),('14', ' enter partner'),('15', 'breakup partnership'),('16', 'change businessname'),('17', 'transfer_ownership'),('18', ' reissued request'),('19', 'cancel license')],string='request type')
    decision_details = fields.One2many('decisions.decisions', 'project_id','')



    ##################################################
    docs = fields.One2many('request.attachmens','profile','docs')


    #################################################
    area = fields.Char(string='area')
    land_number = fields.Char(string='land number')
    square = fields.Char(string='square')
    coordinates = fields.Char()



    #####################################
    visit_number = fields.Char('')
    visit_type = fields.Char('')    
    visit_date = fields.Date('')
    visit_details = fields.One2many('field.visit','project_id', '')
    



    ########################################
    owners = fields.One2many('nia.owners','profile','owners')



    #####################################
    file_number = fields.Char('')
    box_number = fields.Char('')
    


