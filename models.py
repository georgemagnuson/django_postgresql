# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DbItems(models.Model):
    uuid = models.UUIDField(primary_key=True)
    description = models.CharField(blank=True, null=True)
    unit_of_measure_text = models.CharField(blank=True, null=True)
    link_to_category = models.ForeignKey('DbItemsCategory', models.DO_NOTHING, db_column='link_to_category', blank=True, null=True, db_comment='can be INGREDIENT category')
    recipe_yield = models.IntegerField(blank=True, null=True)
    recipe_unit_of_measure = models.CharField(max_length=9, blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    unit_of_measure_uuid = models.UUIDField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_items'


class DbItemsCategory(models.Model):
    field_uuid_kplt = models.UUIDField(db_column='_UUID__kplt', primary_key=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    categoryname_xlt = models.CharField(db_column='categoryname__xlt', max_length=1024, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'db_items_category'


class DbItemsRecipeIngredients(models.Model):
    uuid = models.UUIDField()
    link_to_recipe = models.ForeignKey(DbItems, models.DO_NOTHING, db_column='link_to_recipe')
    link_to_item = models.ForeignKey(DbItems, models.DO_NOTHING, db_column='link_to_item', related_name='dbitemsrecipeingredients_link_to_item_set')
    ingredient_qty = models.FloatField(blank=True, null=True)
    ingredient_unit_of_measure = models.UUIDField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_items_recipe_ingredients'


class DbItemsWastageRecord(models.Model):
    uuid = models.UUIDField(unique=True)
    link_to_item_uuid = models.ForeignKey(DbItems, models.DO_NOTHING, db_column='link_to_item_uuid')
    recorded_by = models.CharField()
    date_recorded = models.DateField()
    quantity_gross = models.FloatField(blank=True, null=True)
    quantity_net = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=79, blank=True, null=True)
    entry_date = models.CharField(max_length=10, blank=True, null=True)
    deleted_entry = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'db_items_wastage_record'


class DbRestaurant(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField()
    address = models.CharField()
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_restaurant'


class DbRestaurantLocations(models.Model):
    uuid = models.UUIDField(primary_key=True)
    link_to_restaurant_uuid = models.ForeignKey(DbRestaurant, models.DO_NOTHING, db_column='link_to_restaurant_uuid')
    name = models.CharField()
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_restaurant_locations'


class DbSuppliers(models.Model):
    uuid = models.UUIDField(unique=True)
    name = models.CharField(primary_key=True)
    price_includes_gst = models.CharField(db_column='price_includes_GST')  # Field name made lowercase.
    includes_gst = models.BooleanField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_suppliers'


class DbSuppliersInvoices(models.Model):
    uuid = models.UUIDField(primary_key=True)
    link_to_supplier_uuid = models.ForeignKey(DbSuppliers, models.DO_NOTHING, db_column='link_to_supplier_uuid', to_field='uuid', blank=True, null=True)
    invoice_number = models.CharField()
    invoice_date = models.DateField(blank=True, null=True)
    invoice_date_text = models.CharField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)
    supplier_issuer = models.CharField(blank=True, null=True)
    invoice_amount = models.FloatField(blank=True, null=True)
    invoice_amount_untaxed = models.FloatField(blank=True, null=True)
    statement = models.BooleanField(blank=True, null=True)
    credit = models.BooleanField(blank=True, null=True)
    data_json = models.TextField(blank=True, null=True, db_comment='contents of attachment extracted by invoice2data as json format')  # This field type is a guess.
    gmail_message_id = models.CharField(blank=True, null=True, db_comment='source of truth for invoice data is gmail invoice')

    class Meta:
        managed = False
        db_table = 'db_suppliers_invoices'
        unique_together = (('link_to_supplier_uuid', 'invoice_number'),)


class DbSuppliersInvoicesEntries(models.Model):
    uuid = models.UUIDField(primary_key=True)
    link_to_supplier_item_uuid = models.ForeignKey('DbSuppliersItems', models.DO_NOTHING, db_column='link_to_supplier_item_uuid', blank=True, null=True)
    link_to_supplier_invoice_uuid = models.ForeignKey(DbSuppliersInvoices, models.DO_NOTHING, db_column='link_to_supplier_invoice_uuid', blank=True, null=True)
    quantity_purchased = models.FloatField(blank=True, null=True)
    item_price = models.FloatField(blank=True, null=True)
    item_discount = models.FloatField(blank=True, null=True)
    gross_weight = models.FloatField(blank=True, null=True)
    waste_weight = models.FloatField(blank=True, null=True)
    link_to_supplier_uuid = models.UUIDField(blank=True, null=True)
    link_to_jitsu_item = models.UUIDField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)
    supplier_item_code = models.CharField(blank=True, null=True)
    supplier_item_description = models.CharField(blank=True, null=True)
    item_unit_of_purchase = models.CharField(blank=True, null=True)
    line_total = models.FloatField(blank=True, null=True)
    servings = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_suppliers_invoices_entries'


class DbSuppliersItems(models.Model):
    uuid = models.UUIDField(primary_key=True)
    link_to_supplier_uuid = models.ForeignKey(DbSuppliers, models.DO_NOTHING, db_column='link_to_supplier_uuid', to_field='uuid', blank=True, null=True)
    supplied_item_unit_of_measure_text = models.TextField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    link_to_item_uuid = models.ForeignKey(DbItems, models.DO_NOTHING, db_column='link_to_item_uuid', blank=True, null=True)
    supplied_item_unit_of_measure_uuid = models.UUIDField(blank=True, null=True)
    supplier_item_code = models.CharField(blank=True, null=True)
    supplier_item_description = models.CharField(blank=True, null=True)
    notes = models.CharField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_suppliers_items'


class DbUnitOfMeasure(models.Model):
    uuid = models.UUIDField(primary_key=True)
    long_name = models.CharField(blank=True, null=True)
    short_name = models.CharField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_unit_of_measure'


class DbUnitOfMeasureExchangeRate(models.Model):
    uuid = models.UUIDField(primary_key=True)
    primary_uom = models.ForeignKey(DbUnitOfMeasure, models.DO_NOTHING, db_column='primary_uom', blank=True, null=True)
    target_uom = models.ForeignKey(DbUnitOfMeasure, models.DO_NOTHING, db_column='target_uom', related_name='dbunitofmeasureexchangerate_target_uom_set', blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    deleted_entry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_unit_of_measure_exchange_rate'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IngredientIngredient(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=55)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient_ingredient'


class IngredientIngredientlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit_of_measure = models.CharField(max_length=55)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    component_ingredient = models.ForeignKey(IngredientIngredient, models.DO_NOTHING)
    parent_ingredient = models.ForeignKey(IngredientIngredient, models.DO_NOTHING, related_name='ingredientingredientlist_parent_ingredient_set')

    class Meta:
        managed = False
        db_table = 'ingredient_ingredientlist'


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True)
    gmail_message = models.ForeignKey('Message', models.DO_NOTHING, to_field='gmail_message_id', blank=True, null=True)
    invoice_date = models.DateField()
    invoice_issuer = models.ForeignKey('XSupplierV00', models.DO_NOTHING, db_column='invoice_issuer', to_field='name', blank=True, null=True)
    invoice_supplier_uuid = models.UUIDField(blank=True, null=True)
    invoice_number = models.CharField()
    invoice_amount_gross = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_amount_gst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_amount_net = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_credit = models.BooleanField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class Invoiceentry(models.Model):
    id = models.UUIDField(primary_key=True)
    gmail_message_id = models.CharField(blank=True, null=True)
    entry_supplier_item_code = models.CharField(blank=True, null=True)
    entry_jitsu_item_code = models.ForeignKey('Jitsuitem', models.DO_NOTHING, db_column='entry_jitsu_item_code', blank=True, null=True)
    entry_supplier_description = models.CharField(blank=True, null=True)
    entry_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_unit_of_purchase = models.CharField(blank=True, null=True)
    entry_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_gross_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_net_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_number_of_pieces = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    supplier_uuid = models.UUIDField(blank=True, null=True)
    supplier_item_uuid = models.UUIDField(blank=True, null=True)
    entry_waste_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoiceentry'


class InvoiceentryOld(models.Model):
    id = models.UUIDField(blank=True, null=True)
    invoice_id = models.UUIDField(blank=True, null=True)
    supplier_uuid = models.UUIDField(blank=True, null=True)
    entry_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_gross_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_waste_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    entry_supplier_item_code = models.CharField(blank=True, null=True)
    entry_supplier_description = models.CharField(max_length=1024, blank=True, null=True)
    entry_jitsu_item_code = models.UUIDField(blank=True, null=True)
    supplier_item_uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoiceentry_old'


class Jitsuingredient(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    link_to_ingredient = models.ForeignKey('Jitsuitem', models.DO_NOTHING, db_column='link_to_Ingredient')  # Field name made lowercase.
    quantity_used = models.FloatField(blank=True, null=True)
    recipe_uuid = models.ForeignKey('Jitsuitem', models.DO_NOTHING, db_column='recipe_uuid', related_name='jitsuingredient_recipe_uuid_set')
    unit_of_measure_xlt = models.CharField(db_column='unit_of_measure__xlt', max_length=1024, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'jitsuingredient'


class Jitsuitem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    description = models.CharField()
    category = models.ForeignKey('Jitsuitemcategory', models.DO_NOTHING, db_column='category', blank=True, null=True)
    unit_of_measure = models.CharField(blank=True, null=True)
    cost_per_unit_of_measure = models.FloatField(blank=True, null=True)
    alternate = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jitsuitem'


class Jitsuitemcategory(models.Model):
    uuid = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    description = models.CharField()

    class Meta:
        managed = False
        db_table = 'jitsuitemcategory'


class Message(models.Model):
    id = models.UUIDField(primary_key=True)
    gmail_message_id = models.CharField(unique=True, blank=True, null=True)
    message_date = models.DateField(blank=True, null=True)
    message_from = models.CharField(blank=True, null=True)
    message_to = models.CharField(blank=True, null=True)
    message_subject = models.CharField(blank=True, null=True)
    message_raw = models.CharField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True, db_comment='instead of deleting just check this')
    message_has_attachments = models.BooleanField(blank=True, null=True)
    message_processed = models.BooleanField(blank=True, null=True)
    message_status = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Sqlmodelbase(models.Model):
    uuid = models.UUIDField(primary_key=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_deleted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sqlmodelbase'


class Supplier(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    includes_gst_in_prices = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Supplieritem(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    supplier_uuid = models.ForeignKey('XSupplierV00', models.DO_NOTHING, db_column='supplier_uuid', blank=True, null=True)
    supplier_item_code = models.CharField(blank=True, null=True)
    supplier_item_description = models.CharField(blank=True, null=True)
    jitsu_item_uuid = models.ForeignKey(Jitsuitem, models.DO_NOTHING, db_column='jitsu_item_uuid', blank=True, null=True)
    unit_of_purchase = models.CharField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplieritem'
        unique_together = (('supplier_uuid', 'supplier_item_code'),)


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class TaxRate(models.Model):
    uuid = models.UUIDField(primary_key=True)
    date_begin = models.DateField(db_comment='starting date of tax')
    date_end = models.DateField(blank=True, null=True, db_comment='ending date of tax')
    tax_name = models.CharField(max_length=20)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_rate'


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_deleted = models.DateTimeField(blank=True, null=True)
    username = models.TextField()
    password_hashed = models.TextField()
    user_role = models.ForeignKey('Userrole', models.DO_NOTHING, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    user_role_int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Userrole(models.Model):
    description = models.CharField()
    id = models.UUIDField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    date_deleted = models.DateTimeField(blank=True, null=True)
    user_role_int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userrole'


class XSupplierItemsOld(models.Model):
    id = models.UUIDField(primary_key=True)
    link_to_supplier_uuid = models.ForeignKey('XSuppliersOld', models.DO_NOTHING, db_column='link_to_supplier_uuid', blank=True, null=True)
    supplied_item_unit_of_measure_text = models.TextField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    link_to_item_uuid = models.UUIDField(blank=True, null=True)
    supplied_item_unit_of_measure_uuid = models.UUIDField(blank=True, null=True)
    supplier_item_code = models.CharField(blank=True, null=True)
    supplier_item_description = models.CharField(blank=True, null=True)
    notes = models.CharField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x_supplier_items_old'


class XSupplierV00(models.Model):
    id = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    name = models.CharField(unique=True, blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    includes_gst_in_prices = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'x_supplier_v00'


class XSupplieritemEmpty(models.Model):
    uuid = models.UUIDField(primary_key=True)
    supplier_item_code = models.CharField(blank=True, null=True)
    supplier_item_description = models.CharField(blank=True, null=True)
    unit_of_purchase = models.CharField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.FloatField(blank=True, null=True)
    jitsuitem_uuid = models.ForeignKey(Jitsuitem, models.DO_NOTHING, db_column='jitsuitem_uuid', blank=True, null=True)
    supplier_uuid = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='supplier_uuid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x_supplieritem_empty'
        unique_together = (('uuid', 'supplier_item_code'),)


class XSuppliersOld(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    price_includes_gst = models.CharField(db_column='price_includes_GST', blank=True, null=True)  # Field name made lowercase.
    includes_gst_in_prices = models.BooleanField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x_suppliers_old'
