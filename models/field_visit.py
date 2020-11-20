#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class field_visit(models.Model):
    _name = 'field.visit'
    _rec_name = 'visit_number'

    company_id = fields.Many2one(
        string='Company', 
        comodel_name='res.company', 
        required=True, 
        default=lambda self: self.env.user.company_id
    )

    visit_number = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('increment_field_visit'))
    visit_type = fields.Selection([('1', 'survey'), ('2', 'enclose'),('3', 'treatment')],'')
    visit_date = fields.Date('',default=fields.Date.today)
    section = fields.Many2one('nia.section', 'section')
    project_id = fields.Many2one('res.partner', 'project')
    projct_number = fields.Integer('',related='project_id.projct_number')
    projct_state = fields.Selection([('1', 'active'), ('2', 'inactive')],'')


    area = fields.Char(string='area')
    land_number = fields.Char(string='land number')
    square = fields.Char(string='square')
    total_area = fields.Char('')
    construction_ratio = fields.Char('')
    land_ownership = fields.Selection([('1', 'owner'), ('2', 'rent'),('3', 'specified')],'')
    cost = fields.Char('')
    construction_position = fields.Selection([('1', 'Under construction'), ('2', 'Constructor'),('3', 'Walled'),('4', 'Empty')],'')
    description_buildings = fields.Text('')
    


    waste_type = fields.Selection([('1', 'liquid'), ('2', 'Solid'),('3', 'Gaseous')],'')
    description_waste = fields.Char('')
    disposal_methods = fields.Char('')
    initial_treatment = fields.Selection([('1', 'yes'), ('2', 'no'),],'')
    water_sources = fields.Selection([('1', 'national network'), ('2', 'Well'),('3', 'both')],'')
    electric_sources = fields.Selection([('1', 'national network'), ('2', 'Generators'),('3', 'Solar energy')],'')
    competent_authority_confirm = fields.Selection([('1', 'yes'), ('2', 'no')],'')
    quality_control_laboratory = fields.Selection([('1', 'yes'), ('2', 'no'),],'')
    Problems = fields.Selection([('1', 'Security'), ('2', 'Technical'),('3', 'Finance'),('4', 'Administrative'),('5', 'non')],'')
    description_Problems = fields.Text('')
    
    
    workflow = fields.Selection([('1', 'continued'), ('2', 'Final discontinued'),('3', ' Temporarily discontinued'),('4', 'Production did not start'),('5', 'Buildings without production line')],'')
    discontinuation_date = fields.Date('',default=fields.Date.today)
    start_production = fields.Date('',default=fields.Date.today)
    reasons_for_stopping = fields.Selection([('2', 'Technical'),('3', 'Finance'),('4', 'Administrative'),('5', 'Social')],'')
    description_reasons = fields.Text('')    
    solutions = fields.Text('')    
    
    Machine_origin = fields.Many2one('nia.nationality','')
    machinists_cost = fields.Char('')
    national_workers = fields.Char('')
    foreign_workers = fields.Char('')
    fixed_workers = fields.Char('')
    temporarily_workers = fields.Char('')
    males_workers = fields.Char('')
    females_workers = fields.Char('')
    shifts_number = fields.Char('')   
    shifts_time = fields.Char('')
   
    
    
    raw_material = fields.Many2many('raw.material', 'description')
    products = fields.Many2many('product', 'products')
    team_members = fields.Many2many('team.members', '')

    
    def update_profile(self):
        profile_visit = self.env['res.partner'].search([('id','=',self.project_id.id)])
        for visit in profile_visit:
            visit.visit_details = [(4,self.id)] 
            #vals = { 'visit_details': [1,self.id]}
            #visit_details = rec.write(vals)
            print ('*******************   visit_details           *******************',visit.visit_details)










class team_members(models.Model):
    _name = 'team.members'

    name = fields.Char('')
    comment = fields.Text('')
    




class raw_material(models.Model):
    _name = 'raw.material'

    name = fields.Char('')
    quantity = fields.Char('')
    cost = fields.Char('')
    origin = fields.Many2one('nia.nationality','')

    
    
class product(models.Model):
    _name = 'product'

    name = fields.Char('')
    productive_unit = fields.Many2one('productive.unit', 'productive_unit')
    weights_unit = fields.Many2one('weights.unit', 'weights_unit')
    weight_produced_unit = fields.Char('')
    design_energy = fields.Char('')
    available_energy = fields.Char('')
    productivity_energy = fields.Char('')
    
    team_note = fields.Text('')
    
    
    
      



class productive_unit(models.Model):
    _name = 'productive.unit'

    name = fields.Char('') 


class weights_unit(models.Model):
    _name = 'weights.unit'

    name = fields.Char('') 