# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import  ValidationError

class FieldsImport(models.Model):
    _name = 'import_adj.fields_import'
    id_char = fields.Char()
    name = fields.Char()
    column1 = fields.Char()
    column2 = fields.Char()
    complete_name = fields.Char()
    compute = fields.Char()
    copy = fields.Char()
    depends = fields.Char()
    domain = fields.Char()
    field_description = fields.Char()
    groups = fields.Char()
    help = fields.Char()
    index = fields.Char()
    model = fields.Char()
    model_id = fields.Char()
    modules = fields.Char()
    on_delete = fields.Char()
    readonly = fields.Char()
    related = fields.Char()
    relation = fields.Char()
    relation_field = fields.Char()
    relation_table = fields.Char()
    required = fields.Char()
    selectable = fields.Char()
    selection = fields.Char()
    size = fields.Char()
    state = fields.Char()
    store = fields.Char()
    translate = fields.Char()
    ttype = fields.Char()
    
    
class ModesImport(models.Model):
    _name = 'import_adj.model_import'
    id_char = fields.Char()
    modules = fields.Char()
    model = fields.Char()
    name = fields.Char()
    transient = fields.Char()


class ActionImport(models.Model):
    _name = 'import_adj.action_import'
    id_char = fields.Char()
    name = fields.Char()
    auto_search = fields.Char()
    context = fields.Char()
    domain = fields.Char()
    filter = fields.Char()
    groups_id = fields.Char()
    limit = fields.Char()
    multi = fields.Char()
    res_id = fields.Char()
    res_model = fields.Char()
    search_view = fields.Char()
    search_view_id = fields.Char()
    src_model = fields.Char()
    target = fields.Char()
    type = fields.Char()
    usage = fields.Char()
    view_id = fields.Char()
    view_ids = fields.Char()
    view_mode = fields.Char()
    view_type = fields.Char()
    views = fields.Char()

    
class MenuImport(models.Model):
    _name = 'import_adj.menu_import'
    #_name*ir.ui.menu
    
    id_char = fields.Char()
    action = fields.Char()
    active = fields.Char()
    child_id = fields.Char()
    complete_name = fields.Char()
    groups_id = fields.Char()
    name = fields.Char()
    parent_id = fields.Char()
    parent_left = fields.Char()
    parent_right = fields.Char()
    sequence = fields.Char()
    web_icon = fields.Char()
    web_icon_data = fields.Char()
    

class ViewImport(models.Model):
    _name = 'import_adj.view_import'
    #_name*ir.ui.view
    id_char = fields.Char()
    arch = fields.Char()
    arch_base = fields.Char()
    arch_db = fields.Char()
    arch_fs = fields.Char()
    create_date = fields.Char()
    field_parent = fields.Char()
    groups_id = fields.Char()
    inherit_children_ids = fields.Char()
    inherit_id = fields.Char()
    key = fields.Char()
    mode = fields.Char()
    model = fields.Char()
    model_data_id = fields.Char()
    model_ids = fields.Char()
    name = fields.Char()
    priority = fields.Char()
    type = fields.Char()
    write_date = fields.Char()
    xml_id = fields.Char()

    

    
    
    
    
    
    
    
