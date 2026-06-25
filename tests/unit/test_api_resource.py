import unittest
from unittest.mock import MagicMock

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.i_communicator import ICommunicator

class ConcreteApiResource(ApiResource):
    pass

class ApiResourceTest(unittest.TestCase):

    @staticmethod
    def _mock_communicator():
        return MagicMock(spec=ICommunicator)

    def test_ConstructingWithParent_DefaultScenario_ThrowExceptionWhenParentAndCommunicatorAreNull(self):
        with self.assertRaises(ValueError):
            ConcreteApiResource(parent=None, communicator=None)

    def test_ConstructingWithParent_DefaultScenario_CreateInstanceWithParent(self):
        communicator = self._mock_communicator()
        parent = ConcreteApiResource(communicator=communicator, path_context={"id": "123"})
        child = ConcreteApiResource(parent=parent, path_context={})
        self.assertIsNotNone(child)

    def test_ConstructingWithParent_DefaultScenario_InheritCommunicatorFromParent(self):
        communicator = self._mock_communicator()
        parent = ConcreteApiResource(communicator=communicator)
        child = ConcreteApiResource(parent=parent)
        self.assertIs(communicator, child._communicator)

    def test_ConstructingWithParent_DefaultScenario_InheritClientMetaInfoFromParent(self):
        communicator = self._mock_communicator()
        client_meta_info = "test-meta-info"
        parent = ConcreteApiResource(communicator=communicator, client_meta_info=client_meta_info)
        child = ConcreteApiResource(parent=parent)
        self.assertEqual(client_meta_info, child._client_meta_info)

    def test_ConstructingWithParent_DefaultScenario_AcceptNullPathContext(self):
        communicator = self._mock_communicator()
        parent = ConcreteApiResource(communicator=communicator)
        child = ConcreteApiResource(parent=parent, path_context=None)
        self.assertIsNotNone(child)

    def test_ConstructingAsRoot_DefaultScenario_ThrowExceptionWhenCommunicatorIsNull(self):
        with self.assertRaises(ValueError):
            ConcreteApiResource(communicator=None)

    def test_ConstructingAsRoot_DefaultScenario_CreateInstanceWithValidCommunicator(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator)
        self.assertIsNotNone(resource)

    def test_ConstructingAsRoot_DefaultScenario_StoreCommunicator(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info="meta")
        self.assertIs(communicator, resource._communicator)

    def test_ConstructingAsRoot_DefaultScenario_StoreClientMetaInfo(self):
        communicator = self._mock_communicator()
        client_meta_info = "custom-meta-info"
        resource = ConcreteApiResource(communicator=communicator, client_meta_info=client_meta_info)
        self.assertEqual(client_meta_info, resource._client_meta_info)

    def test_ConstructingAsRoot_DefaultScenario_AcceptNullClientMetaInfo(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info=None)
        self.assertIsNone(resource._client_meta_info)

    def test_ConstructingAsRoot_DefaultScenario_AcceptNullPathContext(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info="meta", path_context=None)
        self.assertIsNotNone(resource)

    def test_GettingClientHeaders_DefaultScenario_ReturnNullWhenClientMetaInfoIsNull(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info=None)
        self.assertIsNone(resource._client_headers)

    def test_GettingClientHeaders_DefaultScenario_ReturnHeaderListWhenClientMetaInfoProvided(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info="test-meta-info")
        headers = resource._client_headers
        self.assertEqual(1, len(headers))

    def test_GettingClientHeaders_DefaultScenario_HaveCorrectHeaderName(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info="meta")
        headers = resource._client_headers
        self.assertEqual("X-GCS-ClientMetaInfo", headers[0].name)

    def test_GettingClientHeaders_DefaultScenario_HaveCorrectHeaderValue(self):
        communicator = self._mock_communicator()
        client_meta_info = "my-custom-meta-info"
        resource = ConcreteApiResource(communicator=communicator, client_meta_info=client_meta_info)
        headers = resource._client_headers
        self.assertEqual(client_meta_info, headers[0].value)

    def test_GettingClientHeaders_DefaultScenario_ReturnNewListEachTime(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, client_meta_info="meta")
        headers1 = resource._client_headers
        headers2 = resource._client_headers
        self.assertIsNot(headers1, headers2)

    def test_InstantiatingUri_DefaultScenario_ReplaceSinglePathPlaceholder(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"id": "123"})
        result = resource._instantiate_uri("/api/{id}/details", {})
        self.assertEqual("/api/123/details", result)

    def test_InstantiatingUri_DefaultScenario_ReplaceMultiplePlaceholders(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"version": "v1", "resource": "payments"})
        result = resource._instantiate_uri("/{version}/{resource}", {})
        self.assertEqual("/v1/payments", result)

    def test_InstantiatingUri_DefaultScenario_HandleNullPathContext(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context=None)
        result = resource._instantiate_uri("/api/resource", {})
        self.assertEqual("/api/resource", result)

    def test_InstantiatingUri_DefaultScenario_ReplaceFromSuppliedContext(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={})
        result = resource._instantiate_uri("/user/{id}/profile", {"id": "456"})
        self.assertEqual("/user/456/profile", result)

    def test_InstantiatingUri_DefaultScenario_HandleUriWithoutPlaceholders(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={})
        result = resource._instantiate_uri("/api/resource", {})
        self.assertEqual("/api/resource", result)

    def test_InstantiatingUri_DefaultScenario_ChainParentInstantiation(self):
        communicator = self._mock_communicator()
        parent = ConcreteApiResource(communicator=communicator, path_context={"tenantId": "tenant-001"})
        child = ConcreteApiResource(parent=parent, path_context={"resourceId": "resource-123"})
        result = child._instantiate_uri("/tenants/{tenantId}/resources/{resourceId}", {})
        self.assertEqual("/tenants/tenant-001/resources/resource-123", result)

    def test_ReplacingPathContext_DefaultScenario_ReplaceAllOccurrencesOfPlaceholder(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"id": "999"})
        result = resource._instantiate_uri("/{id}/nested/{id}/deep", {})
        self.assertEqual("/999/nested/999/deep", result)

    def test_ReplacingPathContext_DefaultScenario_PreservePlaceholdersNotInContext(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"id": "123"})
        result = resource._instantiate_uri("/{id}/{unknown}", {})
        self.assertEqual("/123/{unknown}", result)

    def test_ReplacingPathContext_DefaultScenario_HandleEmptyPathContext(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={})
        result = resource._instantiate_uri("/api/{id}/resource", {})
        self.assertEqual("/api/{id}/resource", result)

    def test_ReplacingPathContext_DefaultScenario_HandleSpecialCharactersInValues(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"id": "abc-123-def"})
        result = resource._instantiate_uri("/resource/{id}/detail", {})
        self.assertEqual("/resource/abc-123-def/detail", result)

    def test_ReplacingPathContext_DefaultScenario_HandleNumericValues(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"version": "2", "id": "12345"})
        result = resource._instantiate_uri("/v{version}/resource/{id}", {})
        self.assertEqual("/v2/resource/12345", result)

    def test_InstantiatingUri_DefaultScenario_UseResourcePathContextFirst(self):
        communicator = self._mock_communicator()
        resource = ConcreteApiResource(communicator=communicator, path_context={"id": "parent-123"})
        result = resource._instantiate_uri("/{id}", {"id": "override-456"})
        self.assertEqual("/override-456", result)

if __name__ == '__main__':
    unittest.main()
