from odoo import models, fields, api
import datetime
from builtins import filter
from operator import itemgetter
from odoo.addons.base.ir.ir_ui_view import  View
from odoo.exceptions import UserError



    
NOT_IN =  ['__last_update', 'create_date', 'create_uid', 'display_name', 'id', 'write_date', 'write_uid']

def convert_to_python_fields(name,ttype, relation,relation_field,related):
#             ttype = db_field.ttype
#             tType = ttype.capitalize()
#             relation = db_field.relation # for m2o,m2m,o2m
#             relation_field = db_field.relation_field # for o2m
#             related = db_field.related
            ttype = ttype.capitalize()
            
            tType = 'fields.%s'%ttype
            
            alist = []
            if ttype =='Selection':
                alist.append("[('1','1')]")
            if relation:
                alist.append("'%s'"%relation)
            if relation_field:
                alist.append("'%s'"%relation_field)
            if related:
                alist.append("%s='%s'"%('related', related))
            argument = ', '.join(["%s"%x for x in alist])
            declare = '%s = %s(%s)'%(name, tType, argument)
            return declare
        
def af(self,read_group_rs):
    for i in read_group_rs:
        model_id = i['model_id']
#             fields_ids = self.env['import_adj.fields_import'].search([('model_id','=',model_id)])
#             fields_ids_char = str(fields_ids.mapped('name'))
        model_id_obj = self.env['import_adj.model_import'].search([('id_char','=',model_id)])
        if model_id_obj:
            model_name_class = model_id_obj.name
            model_name = model_id_obj.model
            name_or_inherit = '_name'
        else:
            module_name_and_model_name = model_id.split('.')
            module_name = module_name_and_model_name[0]
            model_name = module_name_and_model_name[1]
            
            rs = self.env['ir.model.data'].search([('name','=',model_name)])[0]
            model_name = model_name[6:]
            model_name = model_name.replace('_',' ')
            model_name_class = module_name+ ' ' + model_name
            model_name_class = model_name_class.title()
#             model_name = model_name.replace(' ','.')
            model_name = self.env['ir.model'].browse(rs.res_id).model
            name_or_inherit = '_inherit'
            
        i['name_or_inherit']  = name_or_inherit
        i['model_name_class'] = model_name_class
        i['model_name']=model_name
            
    return read_group_rs   
def escapse_xml(val):  
    return val.replace('&','&amp;')
class Todo(models.Model):
    _name = 'import_adj.model_gen'
#     _rec_name = 'description'
    pre_models = fields.Text()
    models = fields.Text()
    models_ids = fields.Many2many('ir.model')
    test2= fields.Text()
    test = fields.Text()
#     @staticmethod
#     def search_a_text_model(i):
#         self.env['ir.model'].search([()])

    
    def gen_action(self):
#         template = '''<record id="%(id_char)s" model="ir.actions.act_window">
#          <field name="name">%(name)s</field>
#          <field name="res_model">%(res_model)s</field>
#          <field name="view_type">%(view_type)s</field>
#          <field name="view_mode">tree,form</field>
#          <field name="domain">%(domain)s</field>
#          <field name="context">%(context)s</field>
#       </record>'''
        
        template = '''<record id="%(id_char)s" model="ir.actions.act_window">
         <field name="name">%(name)s</field>
         <field name="res_model">%(res_model)s</field>
         <field name="view_type">%(view_type)s</field>
         <field name="view_mode">tree,form</field>
      </record>'''
        
        
        def a_gen_action(action):
            def tupple_things (afield):
                if isinstance(afield, tuple):
                    field_name  = afield[0]
                    func = afield[1].get('func')
                else:
                    field_name = afield
                    func = None
                val =  getattr(action, field_name)
                val = escapse_xml(str(val))
                if func:
                    val = func(val)
                return (field_name,val)
            
            
            al = ['id_char', 'name', 'res_model', ('view_type',{'func':lambda v: v.lower()}), 'domain', 'context'  ]
            rs = list(map(tupple_things, al))
            print ('88888 rs', rs)
            rs = dict(rs)
            return template%rs
        actions = self.env['import_adj.action_import'].search([('id_char','=ilike','tour_travel.%')])
        rs = map(a_gen_action,actions)
        t2 = '''<odoo>
    <data>
    %s
    </data>
</odoo>'''
        print('***rs', rs)
        va = '\n'.join(rs)
        print ('***2', va)
        self.test2 =t2%va
        pass
    def gen_view(self):
        template = '''<record id="%(id_char)s" model="ir.ui.view">
         <field name="name">%(name)s</field>
         <field name="model">%(model)s</field>
         <field name="type">%(type)s</field>%(inherit_id)s
         <field name="priority">%(priority)s</field>
         <field name="arch" type="xml">%(arch_db)s
         </field>
</record>'''
        
#         raise UserError(View._fields['type'].get_description(self.env)['selection'])
        TYPE = [         ('tree', 'Tree'),
                             ('form', 'Form'),
                             ('graph', 'Graph'),
                             ('pivot', 'Pivot'),
                             ('calendar', 'Calendar'),
                             ('diagram', 'Diagram'),
                             ('gantt', 'Gantt'),
                             ('kanban', 'Kanban'),
                             ('search', 'Search'),
                             ('qweb', 'QWeb')]
        TYPE = [(i[1],i[0]) for i in TYPE]
        TYPE = dict(TYPE)
        MODE = [('primary', "Base view"), ('extension', "Extension View")]
        MODE = dict([('primary', "Base view"), ('extension', "Extension View")])
        
        tpl_inherit = '''<field name="inherit_id" ref="%s"/>
        '''
        def inherit_id_(v):
            v =  '' if (not v or v=='0' or v=='False') else tpl_inherit%v
            return v
            
            
        def a_gen_xml(action):
            def create_context_for_template (afield):
                if isinstance(afield, tuple):
                    field_name  = afield[0]
                    func = afield[1].get('func')
                    no_escapse = afield[1].get('no_escapse')
                else:
                    field_name = afield
                    func = None
                    no_escapse = False
                val =  getattr(action, field_name)
                if not no_escapse:
                    val = escapse_xml(str(val))
                if func:
                    val = func(val)
                return (field_name,val)
            fields = ['id_char', 'name', ('type',{'func':lambda v:TYPE[v]}), ('model',{'func':lambda v: '' if v =='False' else v}), ('priority',{'func':lambda v: int(float(v)) }),
                        ('inherit_id',{'func': inherit_id_}),('arch_db',{'no_escapse':True})]
            fields_context_list_of_tuple = list(map(create_context_for_template, fields))
            dict_fields_context= dict(fields_context_list_of_tuple)
            return template%dict_fields_context
        
        obj_list = self.env['import_adj.view_import'].search([('id_char','=ilike','tour_travel.%')])
        rs = map(a_gen_xml, obj_list)
        t2 = '''<odoo>
    <data>
    %s
    </data>
</odoo>'''
        va = '\n'.join(rs)
        self.test2 =t2%va
    def gen_menu(self):
        template = '''<menuitem id="%(id_char)s" name="%(name)s" parent="%(parent_id)s"  action="%(action)s" sequence="%(sequence)s"/>'''
        def a_gen_xml(action):
            def create_context_for_template (afield):
                if isinstance(afield, tuple):
                    field_name  = afield[0]
                    func = afield[1].get('func')
                else:
                    field_name = afield
                    func = None
                val =  getattr(action, field_name)
                val = escapse_xml(str(val))
                if func:
                    val = func(val)
                return (field_name,val)
            fields = ['id_char', 'name',('action',{'func':lambda v: '' if v =='False' else v}), ('sequence',{'func':lambda v: int(float(v))}),('parent_id',{'func':lambda v: '' if v =='False' else v})]
            fields_context_list_of_tuple = list(map(create_context_for_template, fields))
            dict_fields_context= dict(fields_context_list_of_tuple)
            return template%dict_fields_context
        
        obj_list = self.env['import_adj.menu_import'].search([('id_char','=ilike','tour_travel.%')])
        rs = map(a_gen_xml, obj_list)
        t2 = '''<odoo>
    <data>
    %s
    </data>
</odoo>'''
        va = '\n'.join(rs)
        self.test2 =t2%va
        pass      
            
    
    def test_field(self):
        read_group_rs = self.env['import_adj.fields_import'].read_group([('modules','=ilike','tour_travel')], ['model_id'],['model_id'], lazy=False)
        af(self,read_group_rs)
            
        read_group_rs = sorted(read_group_rs, key=itemgetter('name_or_inherit'))
        rt = ''
        for i in read_group_rs:
            fields_ids = self.env['import_adj.fields_import'].search([('model_id','=',i['model_id'])])
#             model_id = i['model_id']
#             model_id_obj = self.env['import_adj.model_import'].search([('id_char','=',model_id)])
#             if model_id_obj:
#                 model_name_class = model_id_obj.name
#                 model_name = model_id_obj.model
#                 name_or_inherit = '_name'
#             else:
#                 module_name_and_model_name = model_id.split('.')
#                 module_name = module_name_and_model_name[0]
#                 model_name = module_name_and_model_name[1]
#                 model_name = model_name[6:]
#                 model_name = model_name.replace('_',' ')
#                 model_name_class = module_name+ ' ' + model_name
#                 model_name_class = model_name_class.title()
#                 model_name = model_name.replace(' ','.')
#                 name_or_inherit = '_inherit'
                
            name_or_inherit = i['name_or_inherit'] 
            model_name_class = i['model_name_class']
            model_name = i['model_name']
            class_name_declare = model_name_class.replace(' ','').replace('.','')
            class_declare = 'class %s(models.Model):'%class_name_declare
            pre =  class_declare + '\n\t'  + name_or_inherit  + ' = ' +  "'%s'"%model_name + '\n\t'
            if 'name' in name_or_inherit:
                pre+="_inherit = ['mail.thread', 'mail.activity.mixin']" + '\n\t' 
            field_python_list = map(lambda f: convert_to_python_fields(f.name, f.ttype, f.relation, f.relation_field, f.related),fields_ids)
            rt += pre + '\n\t'.join(field_python_list) +'\n\n'
        self.test2 = rt
    def set_list_of_models(self):
        rs = self.pre_models.split('\n')
        rs = list(set(rs))
        self.test2 = rs
    def write(self,vals):
        print ('dung buon em hoi***********')
        rs = models.Model.write(self, vals)
        return rs
        
    
    def test_search(self):
        
        def convert_to_python_fields(db_field):
            ttype = db_field.ttype
            tType = ttype.capitalize()
            relation = db_field.relation # for m2o,m2m,o2m
            relation_field = db_field.relation_field # for o2m
            related = db_field.related
            alist = []
            if relation:
                alist.append(relation)
            if relation_field:
                alist.append(relation_field)
            if related:
                alist.append('%s=%s'%('related', related))
            argument = ', '.join(alist)
            declare = '%s = %s(%s)'%(db_field.name, tType, argument)
            return declare
                
                
            
            
        def search_a_text_model(i):
            print ('akakaka*',i)
            
            if len(i)>3:
                ids = self.env.ref(i).ids
                rs = self.env['ir.model'].search([('id','in',ids)])
                if rs:
#                     adict = {}
#                     for ifield in rs.field_id:
                    list_fields = rs.field_id #
#                     fields_names = list(filter(lambda i: i not in NOT_IN, fields_names ))
                    list_fields = list_fields.filtered(lambda i: i.name not in NOT_IN )
#                     fields_names = list(map(lambda f:(f.name,f.ttype), list_fields) )
                    fields_names = list(map(convert_to_python_fields, list_fields) )
                    return rs.name + ', ' + str(fields_names)
                else:
                    return 'None exit'
            return 'empty'
        rs = self.models.split('\n')
        rs2 = map(search_a_text_model, rs)
        rs2 = list(set(rs2))
        self.test = '\n'.join(rs2)
    