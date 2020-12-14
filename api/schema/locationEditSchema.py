from marshmallow import Schema
from marshmallow import fields


class LocationEditSchema(Schema):
    id = fields.Integer()
    name = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    user_id = fields.Integer(allow_none=True)
    avatar = fields.String(allow_none=True)
    create_at = fields.DateTime(format='iso', dump_only=True)
    update_at = fields.DateTime(format='iso', dump_only=True)

