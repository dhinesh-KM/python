from django.db.backends.base.operations import BaseDatabaseOperations

class CustomDatabaseOperations(BaseDatabaseOperations):
    def datetime_extract_sql(self, lookup_type, field_name):
        if lookup_type == 'year':
            return "EXTRACT(year FROM %s)" % field_name
        elif lookup_type == 'month':
            return "EXTRACT(month FROM %s)" % field_name
        else:
            raise NotImplementedError("Lookup type '%s' not supported." % lookup_type)
