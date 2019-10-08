 # -*- coding: utf-8 -*-
def convert_integer(val,needdata):
    try:
        return int(val)
    except:
        return 0
def int_catch_error_(v,n):
    try:
        v = int(v)
    except:
        v = False
    return v

def float_catch_error_(v,n):
    try:
        v = float(v)
    except:
        v = False
    return v
def gen_dict():
    tvcv_dict = {
          u'fields_import': {
                'title_rows' : range(0,1), 
                'begin_data_row_offset_with_title_row' :1,
                'sheet_names':lambda self,wb: [wb.sheet_names()[0]],
                'model':'import_adj.fields_import',
                'offset_write_xl':1,
                'string':'TVCV da co chua',
                'fields' : [
                        ('id_char', {'xl_title':u'id', 'required':False, 'key':True }),
                        ('model_id', {'xl_title':u'model_id/id', 'required':False, 'key':True }),
                        ('field_description', {'xl_title':u'field_description', 'required':False, 'key':True }),
                        ('name', {'xl_title':u'name', 'required':False, 'key':True }),
                        ('ttype', {'xl_title':u'ttype', 'required':False, 'key':True }),
                        ('readonly', {'xl_title':u'readonly', 'required':False, 'key':True }),
                        ('related', {'xl_title':u'related', 'required':False, 'key':True }),
                        ('relation_field', {'xl_title':u'relation_field', 'required':False, 'key':True }),
                        ('relation_table', {'xl_title':u'relation_table', 'required':False, 'key':True }),
                        ('relation', {'xl_title':u'relation', 'required':False, 'key':True }),
                        ('modules', {'xl_title':u'modules', 'required':False, 'key':True }),
                      ]
                },#End stock.inventory.line'   
                 
                 
             u'model_import': {
                'title_rows' : range(0,1), 
                'begin_data_row_offset_with_title_row' :1,
                'sheet_names':lambda self,wb: [wb.sheet_names()[0]],
                'model':'import_adj.model_import',
                'offset_write_xl':1,
                'string':'TVCV da co chua',
                'fields' : [
                    ('id_char', {'xl_title':u'id', 'required':False, 'key':True }),
                    ('modules', {'xl_title':u'modules', 'required':False, 'key':True }),
                    ('model', {'xl_title':u'model', 'required':False, 'key':True }),
                    ('name', {'xl_title':u'name', 'required':False, 'key':True }),
                    ('transient', {'xl_title':u'transient', 'required':False, 'key':True }),
                      ]
                },#End stock.inventory.line'   
                 
            
            u'action_import': {
                'title_rows' : range(0,1), 
                'begin_data_row_offset_with_title_row' :1,
                'sheet_names':lambda self,wb: [wb.sheet_names()[0]],
                'model':'import_adj.action_import',
                'offset_write_xl':1,
                'string':'TVCV da co chua',
                'fields' : [
                    ('id_char', {'xl_title':u'id', 'required':False, 'key':True }),
                    ('name', {'xl_title':u'name', 'required':False, 'key':True }),
                    ('type', {'xl_title':u'type', 'required':False, 'key':True }),
                    ('usage', {'xl_title':u'usage', 'required':False, 'key':True }),
                    ('auto_search', {'xl_title':u'auto_search', 'required':False, 'key':True }),
                    ('context', {'xl_title':u'context', 'required':False, 'key':True }),
                    ('res_model', {'xl_title':u'res_model', 'required':False, 'key':True }),
                    ('domain', {'xl_title':u'domain', 'required':False, 'key':True }),
                    ('filter', {'xl_title':u'filter', 'required':False, 'key':True }),
                    ('limit', {'xl_title':u'limit', 'required':False, 'key':True }),
                    ('res_id', {'xl_title':u'res_id', 'required':False, 'key':True }),
                    ('multi', {'xl_title':u'multi', 'required':False, 'key':True }),
                    ('src_model', {'xl_title':u'src_model', 'required':False, 'key':True }),
                    ('target', {'xl_title':u'target', 'required':False, 'key':True }),
                    ('view_mode', {'xl_title':u'view_mode', 'required':False, 'key':True }),
                    ('view_type', {'xl_title':u'view_type', 'required':False, 'key':True }),

                      ]
                },#End stock.inventory.line'   
                 
            u'menu_import': {
                'title_rows' : range(0,1), 
                'begin_data_row_offset_with_title_row' :1,
                'sheet_names':lambda self,wb: [wb.sheet_names()[0]],
                'model':'import_adj.menu_import',
                'offset_write_xl':1,
                'string':'TVCV da co chua',
                'fields' : [
                    ('action', {'xl_title':u'action', 'required':False, 'key':True }),
                    ('id_char', {'xl_title':u'id', 'required':False, 'key':True }),
                    ('active', {'xl_title':u'active', 'required':False, 'key':True }),
                    ('name', {'xl_title':u'name', 'required':False, 'key':True }),
                    ('parent_left', {'xl_title':u'parent_left', 'required':False, 'key':True }),
                    ('parent_right', {'xl_title':u'parent_right', 'required':False, 'key':True }),
                    ('sequence', {'xl_title':u'sequence', 'required':False, 'key':True }),
                    ('parent_id', {'xl_title':u'parent_id/id', 'required':False, 'key':True }),



                      ]
                },#End stock.inventory.line'  
                 
                 
                 
                 
        u'view_import': {
                'title_rows' : range(0,1), 
                'begin_data_row_offset_with_title_row' :1,
                'sheet_names':lambda self,wb: [wb.sheet_names()[0]],
                'model':'import_adj.view_import',
                'offset_write_xl':1,
                'string':'TVCV da co chua',
                'fields' : [
                    
                    ('inherit_id', {'xl_title':u'Inherited View old', 'required':False, 'key':True }),
#                     ('inherit_id', {'xl_title':u'Inherited View gốc', 'required':False, 'key':True }),
                    ('id_char', {'xl_title':u'External ID', 'required':False, 'key':True }),
                    ('model', {'xl_title':u'Model', 'required':False, 'key':True }),
                    ('priority', {'xl_title':u'Sequence', 'required':False, 'key':True }),
                    ('name', {'xl_title':u'View Name', 'required':False, 'key':True }),
                    ('type', {'xl_title':u'View Type', 'required':False, 'key':True }),
                    ('arch_db', {'xl_title':u'Arch Blob gốc', 'required':False, 'key':True }),
                    ('arch_fs', {'xl_title':u'Arch Filename', 'required':False, 'key':True }),
                    ('mode', {'xl_title':u'View inheritance mode', 'required':False, 'key':True }),
                      ]
                },#End stock.inventory.line' 
                 
                 
                 
                 
                 
                 
                 
                      
                 
        
         
        }
    return tvcv_dict