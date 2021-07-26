from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("confirm", path="actions/confirm", operations=["create"])
class PortingOrder(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "porting_order"

    def confirm(self, **params):
        return PortingOrder.create_confirm(self.id, **params)


class PortingPhoneNumber(ListableAPIResource):
    OBJECT_NAME = "porting_phone_number"
