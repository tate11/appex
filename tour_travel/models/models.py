# -*- coding: utf-8 -*-

from odoo import models, fields, api
class AccountAccountMove(models.Model):
    _inherit = 'account.move'
    tour_date_id = fields.Many2one('tour.date')

class BaseIrAttachment(models.Model):
    _inherit = 'ir.attachment'
    document_type_id = fields.Many2one('document.type')
    passport_booking_id = fields.Many2one('passport.booking')
    visa_booking_id = fields.Many2one('visa.booking')

class BaseResPartner(models.Model):
    _inherit = 'res.partner'
    is_hotel = fields.Boolean()
    is_transport = fields.Boolean()
    passport_number = fields.Char()
    partner_id = fields.Char()
    passport_expiry_date = fields.Date()
    passport_isue_date = fields.Date()
    date_of_birth = fields.Date()
    passport_ids = fields.One2many('passport', 'partner_id')
    tour_date_ids = fields.One2many('tour.attendee', 'partner_id')
    gender = fields.Selection([('1','1')])

class CrmCrmLead(models.Model):
    _inherit = 'crm.lead'
    product_id = fields.Many2one('product.template')
    tour_date_id = fields.Many2one('tour.date')

class CrmCrmOpportunityReport(models.Model):
    _inherit = 'crm.opportunity.report'
    product_id = fields.Many2one('product.template')
    tour_date_id = fields.Many2one('tour.date')

class ProductProductTemplate(models.Model):
    _inherit = 'product.template'
    duration = fields.Integer()
    departure = fields.Many2one('destination')
    tour_type = fields.Many2one('tour.type')
    product_ids = fields.One2many('tour.product', 'tour_id')
    tour_destination_ids = fields.One2many('tour.destination', 'tour_id')
    tour_program_ids = fields.One2many('tour.program.line', 'tour_id')
    transport_ids = fields.One2many('tour.transport', 'tour_id')
    hotel_ids = fields.One2many('tour.destination.hotel', 'tour_id')
    specific = fields.Selection([('1','1')])

class PurchasePurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    hotel_reservation_id = fields.Many2one('hotel.reservation')
    tour_date_id = fields.Many2one('tour.date')

class Sale_CrmSaleOrder(models.Model):
    _inherit = 'sale.order'
    is_tour_booking = fields.Boolean()
    attendee_count = fields.Integer()
    passport_booking_id = fields.Many2one('passport.booking')
    visa_booking_id = fields.Many2one('visa.booking')
    tour_id = fields.Many2one('product.template')
    tour_date_id = fields.Many2one('tour.date')
    tour_attendee_ids = fields.One2many('tour.attendee', 'sale_order_id')
    book_date = fields.Datetime(related='tour_date_id.book_date')

class StockStockMove(models.Model):
    _inherit = 'stock.move'
    tour_date_id = fields.Many2one('tour.date')

class StockStockPicking(models.Model):
    _inherit = 'stock.picking'
    tour_date_id = fields.Many2one('tour.date')

class TourDestination(models.Model):
    _name = 'destination'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    code = fields.Char()
    city = fields.Char()
    name = fields.Char()
    state_id = fields.Many2one('res.country.state')
    country_id = fields.Many2one('res.country')

class DocumentType(models.Model):
    _name = 'document.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    description = fields.Text()

class HotelClass(models.Model):
    _name = 'hotel.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    description = fields.Char()
    name = fields.Char()

class HotelInformation(models.Model):
    _name = 'hotel.hotel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    hotel_img1 = fields.Binary()
    hotel_img2 = fields.Binary()
    hotel_img3 = fields.Binary()
    hotel_class_id = fields.Many2one('hotel.class')
    partner_id = fields.Many2one('res.partner')
    hotel_room_ids = fields.One2many('hotel.room', 'hotel_id')
    hotel_service_ids = fields.One2many('hotel.service', 'hotel_id')
    name = fields.Char(related='partner_id.name')

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    supplier_ref = fields.Char()
    name = fields.Char()
    date_order = fields.Datetime()
    amount_tax = fields.Float()
    amount_total = fields.Float()
    amount_untaxed = fields.Float()
    company_id = fields.Many2one('res.company')
    pricelist_id = fields.Many2one('product.pricelist')
    user_id = fields.Many2one('res.users')
    currency_id = fields.Many2one('res.currency')
    hotel_id = fields.Many2one('hotel.hotel')
    tour_date_id = fields.Many2one('tour.date')
    reservation_line = fields.One2many('hotel.reservation.line', 'hotel_reservation_id')
    purchase_order_ids = fields.One2many('purchase.order', 'hotel_reservation_id')
    state = fields.Selection([('1','1')])
    notes = fields.Text()
    invoice_ids = fields.Many2many('account.invoice', related='purchase_order_ids.invoice_ids')

class HotelReservationLine(models.Model):
    _name = 'hotel.reservation.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    check_in_date = fields.Date()
    check_out_date = fields.Date()
    price = fields.Float()
    no_of_day = fields.Integer()
    no_of_room = fields.Integer()
    tax_ids = fields.Many2many('account.tax')
    hotel_reservation_id = fields.Many2one('hotel.reservation')
    product_id = fields.Many2one('product.product')
    price_subtotal = fields.Integer()
    price_tax = fields.Integer()
    price_total = fields.Integer()
    name = fields.Text()
    currency_id = fields.Many2one('res.currency', related='hotel_reservation_id.currency_id')

class HotelRoomInformation(models.Model):
    _name = 'hotel.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    description = fields.Char()
    sale_price = fields.Float()
    cost_price = fields.Float()
    room_type_id = fields.Many2one('product.product')
    hotel_id = fields.Many2one('hotel.hotel')
    name = fields.Char(related='room_type_id.name')

class HotelServiceInformation(models.Model):
    _name = 'hotel.service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    description = fields.Char()
    cost_price = fields.Float()
    service_id = fields.Many2one('product.product')
    product_uom = fields.Many2one('product.uom')
    hotel_id = fields.Many2one('hotel.hotel')

class Passport(models.Model):
    _name = 'passport'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    image = fields.Binary()
    image_medium = fields.Binary()
    image_small = fields.Binary()
    name = fields.Char()
    expiry_date = fields.Date()
    issue_date = fields.Date()
    passport_booking_id = fields.Many2one('passport.booking')
    partner_id = fields.Many2one('res.partner')
    visa_ids = fields.One2many('visa', 'passport_id')
    state = fields.Selection([('1','1')])

class PassportBooking(models.Model):
    _name = 'passport.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    passport_number = fields.Char()
    name = fields.Char()
    current_date = fields.Date()
    expiry_date = fields.Date()
    issue_date = fields.Date()
    price = fields.Float()
    customer_id = fields.Many2one('res.partner')
    holder_id = fields.Many2one('res.partner')
    pricelist_id = fields.Many2one('product.pricelist')
    user_id = fields.Many2one('res.users')
    currency_id = fields.Many2one('res.currency')
    product_id = fields.Many2one('product.product')
    attachment_ids = fields.One2many('ir.attachment', 'passport_booking_id')
    document_ids = fields.One2many('passport.booking.document', 'passport_booking_id')
    sale_order_ids = fields.One2many('sale.order', 'passport_booking_id')
    state = fields.Selection([('1','1')])
    email = fields.Char(related='customer_id.email')
    mobile = fields.Char(related='customer_id.mobile')
    invoice_ids = fields.Many2many('account.invoice', related='sale_order_ids.invoice_ids')

class PassportBookingDocument(models.Model):
    _name = 'passport.booking.document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    original_copy = fields.Integer()
    tour_document_type_id = fields.Many2one('document.type')
    passport_booking_id = fields.Many2one('passport.booking')

class reportattendeedeclaration(models.Model):
    _name = 'report.attendee.declaration'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    is_ascii = fields.Boolean()
    partner_ids = fields.Many2many('res.partner')

class TourAttendee(models.Model):
    _name = 'tour.attendee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    sale_order_id = fields.Many2one('sale.order')
    partner_id = fields.Many2one('res.partner')
    attendee_id = fields.Char(related='partner_id.partner_id')
    date_of_birth = fields.Date(related='partner_id.date_of_birth')
    gender = fields.Selection([('1','1')], related='partner_id.gender')
    tour_date_id = fields.Many2one('tour.date', related='sale_order_id.tour_date_id')
    name = fields.Char(related='tour_date_id.name')

class TourDate(models.Model):
    _name = 'tour.date'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    end_date = fields.Datetime()
    start_date = fields.Datetime()
    book_date = fields.Datetime()
    cost_revenue = fields.Float()
    available_seat = fields.Integer()
    lead_count = fields.Integer()
    oppor_count = fields.Integer()
    purchase_order_count = fields.Integer()
    rfq_count = fields.Integer()
    total_seat = fields.Integer()
    tour_booking_count = fields.Integer()
    tour_quotation_count = fields.Integer()
    attendee_count = fields.Integer()
    duration = fields.Integer()
    analytic_account_id = fields.Many2one('account.analytic.account')
    tour_type = fields.Many2one('tour.type')
    tour_id = fields.Many2one('product.template')
    lead_ids = fields.One2many('crm.lead', 'tour_date_id')
    oppor_ids = fields.One2many('crm.lead', 'tour_date_id')
    rfq_ids = fields.One2many('purchase.order', 'tour_date_id')
    tour_booking_ids = fields.One2many('sale.order', 'tour_date_id')
    tour_date_destination_ids = fields.One2many('tour.date.destination', 'tour_date_id')
    tour_date_hotel_ids = fields.One2many('tour.date.destination.hotel', 'tour_date_id')
    tour_date_product_ids = fields.One2many('tour.date.product', 'tour_date_id')
    tour_date_program_ids = fields.One2many('tour.date.program.line', 'tour_date_id')
    tour_date_transport_ids = fields.One2many('tour.date.transport', 'tour_date_id')
    tour_quotation_ids = fields.One2many('sale.order', 'tour_date_id')
    tour_variant_ids = fields.One2many('tour.date.product.variant', 'tour_date_id')
    purchase_order_ids = fields.One2many('purchase.order', 'tour_date_id')
    state = fields.Selection([('1','1')])
    description = fields.Text()

class TourDateDestination(models.Model):
    _name = 'tour.date.destination'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    days = fields.Integer()
    destination_id = fields.Many2one('destination')
    tour_date_id = fields.Many2one('tour.date')
    hotel_ids = fields.One2many('tour.date.destination.hotel', 'tour_date_destination_id')
    city = fields.Char(related='destination_id.city')
    name = fields.Char(related='destination_id.name')
    state_id = fields.Many2one('res.country.state', related='destination_id.state_id')
    country_id = fields.Many2one('res.country', related='destination_id.country_id')

class TourDateDestinationHotel(models.Model):
    _name = 'tour.date.destination.hotel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    auto_booking = fields.Boolean()
    days = fields.Integer()
    tour_date_destination_id = fields.Many2one('tour.date.destination')
    room_id = fields.Many2one('hotel.room')
    hotel_class_id = fields.Many2one('hotel.class')
    hotel_id = fields.Many2one('hotel.hotel')
    tour_date_id = fields.Many2one('tour.date')

class TourDateProduct(models.Model):
    _name = 'tour.date.product'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    product_uom_qty = fields.Float()
    product_id = fields.Many2one('product.product')
    tour_date_id = fields.Many2one('tour.date')
    name = fields.Text()
    product_uom = fields.Many2one('product.uom', related='product_id.product_tmpl_id.uom_id')

class TourDateProductVariant(models.Model):
    _name = 'tour.date.product.variant'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    price = fields.Float()
    qty_booked = fields.Integer()
    uom_id = fields.Many2one('product.uom')
    product_id = fields.Many2one('product.product')
    tour_date_id = fields.Many2one('tour.date')
    name = fields.Text()

class TourDateProgramLine(models.Model):
    _name = 'tour.date.program.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    day = fields.Integer()
    tour_program_id = fields.Many2one('tour.program')
    tour_date_id = fields.Many2one('tour.date')
    breakfast = fields.Boolean(related='tour_program_id.breakfast')
    dinner = fields.Boolean(related='tour_program_id.dinner')
    lunch = fields.Boolean(related='tour_program_id.lunch')

class TourDateTransport(models.Model):
    _name = 'tour.date.transport'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    product_name = fields.Char()
    distance = fields.Float()
    time = fields.Float()
    carrier_id = fields.Many2one('transport.line')
    from_destination = fields.Many2one('destination')
    to_destination = fields.Many2one('destination')
    carrier_line = fields.Many2one('product.product')
    transport_id = fields.Many2one('transport')
    tour_date_id = fields.Many2one('tour.date')

class TourDestination1(models.Model):
    _name = 'tour.destination'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    days = fields.Integer()
    destination_id = fields.Many2one('destination')
    tour_id = fields.Many2one('product.template')
    hotel_ids = fields.One2many('tour.destination.hotel', 'tour_destination_id')
    city = fields.Char(related='destination_id.city')
    name = fields.Char(related='destination_id.name')
    state_id = fields.Many2one('res.country.state', related='destination_id.state_id')
    country_id = fields.Many2one('res.country', related='destination_id.country_id')

class TourDestinationHotel(models.Model):
    _name = 'tour.destination.hotel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    auto_booking = fields.Boolean()
    days = fields.Integer()
    tour_destination_id = fields.Many2one('tour.destination')
    room_id = fields.Many2one('hotel.room')
    hotel_class_id = fields.Many2one('hotel.class')
    hotel_id = fields.Many2one('hotel.hotel')
    tour_id = fields.Many2one('product.template')

class TourProduct(models.Model):
    _name = 'tour.product'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    product_uom_qty = fields.Float()
    tour_id = fields.Many2one('product.template')
    product_id = fields.Many2one('product.product')
    name = fields.Text()
    product_uom = fields.Many2one('product.uom', related='product_id.product_tmpl_id.uom_id')

class TourProgram(models.Model):
    _name = 'tour.program'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    image = fields.Binary()
    image_medium = fields.Binary()
    image_small = fields.Binary()
    breakfast = fields.Boolean()
    dinner = fields.Boolean()
    lunch = fields.Boolean()
    name = fields.Char()
    description = fields.Html()

class TourProgramLine(models.Model):
    _name = 'tour.program.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    day = fields.Integer()
    tour_program_id = fields.Many2one('tour.program')
    tour_id = fields.Many2one('product.template')
    breakfast = fields.Boolean(related='tour_program_id.breakfast')
    dinner = fields.Boolean(related='tour_program_id.dinner')
    lunch = fields.Boolean(related='tour_program_id.lunch')

class TourTransport(models.Model):
    _name = 'tour.transport'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    product_name = fields.Char()
    distance = fields.Float()
    time = fields.Float()
    carrier_id = fields.Many2one('transport.line')
    from_destination = fields.Many2one('destination')
    to_destination = fields.Many2one('destination')
    carrier_line = fields.Many2one('product.product')
    transport_id = fields.Many2one('transport')
    tour_id = fields.Many2one('product.template')

class TourType(models.Model):
    _name = 'tour.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()

class TransportProvider(models.Model):
    _name = 'transport'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    partner_id = fields.Many2one('res.partner')
    transport_line = fields.One2many('transport.line', 'transport_id')
    name = fields.Char(related='partner_id.name')

class TransportCarrierLine(models.Model):
    _name = 'transport.carrier.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    description = fields.Char()
    sale_price = fields.Float()
    cost_price = fields.Float()
    transport_line_id = fields.Many2one('transport.line')
    product_id = fields.Many2one('product.product')
    name = fields.Char(related='product_id.name')

class TransportLine(models.Model):
    _name = 'transport.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    transport_carrier_id = fields.Many2one('res.partner')
    transport_id = fields.Many2one('transport')
    carrier_line = fields.One2many('transport.carrier.line', 'transport_line_id')
    name = fields.Char(related='transport_carrier_id.name')

class Visa(models.Model):
    _name = 'visa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    visa_img = fields.Binary()
    name = fields.Char()
    expiry_date = fields.Date()
    issue_date = fields.Date()
    type_id = fields.Many2one('visa.type')
    passport_id = fields.Many2one('passport')
    visa_booking_id = fields.Many2one('visa.booking')
    country_id = fields.Many2one('res.country')
    partner_id = fields.Many2one('res.partner')
    state = fields.Selection([('1','1')])

class VisaBooking(models.Model):
    _name = 'visa.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    visa_number = fields.Char()
    name = fields.Char()
    current_date = fields.Date()
    expiry_date = fields.Date()
    issue_date = fields.Date()
    price = fields.Float()
    visa_type_id = fields.Many2one('visa.type')
    customer_id = fields.Many2one('res.partner')
    holder_id = fields.Many2one('res.partner')
    passport_id = fields.Many2one('passport')
    pricelist_id = fields.Many2one('product.pricelist')
    user_id = fields.Many2one('res.users')
    currency_id = fields.Many2one('res.currency')
    country_id = fields.Many2one('res.country')
    product_id = fields.Many2one('product.product')
    attachment_ids = fields.One2many('ir.attachment', 'visa_booking_id')
    document_ids = fields.One2many('visa.booking.document', 'visa_booking_id')
    sale_order_ids = fields.One2many('sale.order', 'visa_booking_id')
    state = fields.Selection([('1','1')])
    email = fields.Char(related='customer_id.email')
    mobile = fields.Char(related='customer_id.email')
    invoice_ids = fields.Many2many('account.invoice', related='sale_order_ids.invoice_ids')

class VisaBookingDocument(models.Model):
    _name = 'visa.booking.document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    original_copy = fields.Integer()
    tour_document_type_id = fields.Many2one('document.type')
    visa_booking_id = fields.Many2one('visa.booking')

class VisaType(models.Model):
    _name = 'visa.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    duration = fields.Integer()

