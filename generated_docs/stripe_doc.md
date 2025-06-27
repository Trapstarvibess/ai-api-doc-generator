<p><!DOCTYPE html></p>

<html>
<head>
    <title>Stripe API Documentation</title>
</head>
<body>
    <h1>Stripe API (Version 2025-03-31.basil)</h1>

    <div>
        <h2>GET - /v1/account</h2>
        <p>Retrieve account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/account_links</h2>
        <p>Create an account link</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/account_sessions</h2>
        <p>Create an Account Session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts</h2>
        <p>List all connected accounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return connected accounts that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts</h2>
        <p>No summary available. (AI failed)</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/accounts/{account}</h2>
        <p>Delete an account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}</h2>
        <p>Retrieve account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}</h2>
        <p>Update an account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/bank_accounts</h2>
        <p>Create an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/accounts/{account}/bank_accounts/{id}</h2>
        <p>Delete an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>id (path): Unique identifier for the external account to be deleted.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/bank_accounts/{id}</h2>
        <p>Retrieve an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the external account to be retrieved.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/bank_accounts/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/capabilities</h2>
        <p>List all account capabilities</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/capabilities/{capability}</h2>
        <p>Retrieve an Account Capability</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>capability (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/capabilities/{capability}</h2>
        <p>Update an Account Capability</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>capability (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/external_accounts</h2>
        <p>List all external accounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>object (query): Filter external accounts according to a particular object type.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/external_accounts</h2>
        <p>Create an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/accounts/{account}/external_accounts/{id}</h2>
        <p>Delete an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>id (path): Unique identifier for the external account to be deleted.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/external_accounts/{id}</h2>
        <p>Retrieve an external account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the external account to be retrieved.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/external_accounts/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/login_links</h2>
        <p>Create a login link</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/people</h2>
        <p>List all persons</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>relationship (query): Filters on the list of people returned based on the person's relationship to the account's company.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/people</h2>
        <p>Create a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/accounts/{account}/people/{person}</h2>
        <p>Delete a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/people/{person}</h2>
        <p>Retrieve a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/people/{person}</h2>
        <p>Update a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/persons</h2>
        <p>List all persons</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>relationship (query): Filters on the list of people returned based on the person's relationship to the account's company.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/persons</h2>
        <p>Create a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/accounts/{account}/persons/{person}</h2>
        <p>Delete a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/accounts/{account}/persons/{person}</h2>
        <p>Retrieve a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/persons/{person}</h2>
        <p>Update a person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>person (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/accounts/{account}/reject</h2>
        <p>Reject an account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/apple_pay/domains</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>domain_name (query): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/apple_pay/domains</h2>
        <p>No summary available. (AI failed)</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/apple_pay/domains/{domain}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>domain (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/apple_pay/domains/{domain}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>domain (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/application_fees</h2>
        <p>List all application fees</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (query): Only return application fees for the charge specified by this charge ID.</li>

            <li>created (query): Only return applications fees that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/application_fees/{fee}/refunds/{id}</h2>
        <p>Retrieve an application fee refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>fee (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/application_fees/{fee}/refunds/{id}</h2>
        <p>Update an application fee refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>fee (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/application_fees/{id}</h2>
        <p>Retrieve an application fee</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/application_fees/{id}/refund</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/application_fees/{id}/refunds</h2>
        <p>List all application fee refunds</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/application_fees/{id}/refunds</h2>
        <p>Create an application fee refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/apps/secrets</h2>
        <p>List secrets</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>scope (query): Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/apps/secrets</h2>
        <p>Set a Secret</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/apps/secrets/delete</h2>
        <p>Delete a Secret</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/apps/secrets/find</h2>
        <p>Find a Secret</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>name (query): A name for the secret that's unique within the scope.</li>

            <li>scope (query): Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/balance</h2>
        <p>Retrieve balance</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/balance/history</h2>
        <p>List all balance transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return transactions that were created during the given date interval.</li>

            <li>currency (query): Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payout (query): For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.</li>

            <li>source (query): Only returns the original transaction.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/balance/history/{id}</h2>
        <p>Retrieve a balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/balance_transactions</h2>
        <p>List all balance transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return transactions that were created during the given date interval.</li>

            <li>currency (query): Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payout (query): For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.</li>

            <li>source (query): Only returns the original transaction.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/balance_transactions/{id}</h2>
        <p>Retrieve a balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/alerts</h2>
        <p>List billing alerts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>alert_type (query): Filter results to only include this type of alert.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>meter (query): Filter results to only include alerts with the given meter.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/alerts</h2>
        <p>Create a billing alert</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/alerts/{id}</h2>
        <p>Retrieve a billing alert</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/alerts/{id}/activate</h2>
        <p>Activate a billing alert</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/alerts/{id}/archive</h2>
        <p>Archive a billing alert</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/alerts/{id}/deactivate</h2>
        <p>Deactivate a billing alert</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/credit_balance_summary</h2>
        <p>Retrieve the credit balance summary for a customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): The customer for which to fetch credit balance summary.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>filter (query): The filter criteria for the credit balance summary.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/credit_balance_transactions</h2>
        <p>List credit balance transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>credit_grant (query): The credit grant for which to fetch credit balance transactions.</li>

            <li>customer (query): The customer for which to fetch credit balance transactions.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/credit_balance_transactions/{id}</h2>
        <p>Retrieve a credit balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/credit_grants</h2>
        <p>List credit grants</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): Only return credit grants for this customer.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/credit_grants</h2>
        <p>Create a credit grant</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/credit_grants/{id}</h2>
        <p>Retrieve a credit grant</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/credit_grants/{id}</h2>
        <p>Update a credit grant</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/credit_grants/{id}/expire</h2>
        <p>Expire a credit grant</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/credit_grants/{id}/void</h2>
        <p>Void a credit grant</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meter_event_adjustments</h2>
        <p>Create a billing meter event adjustment</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meter_events</h2>
        <p>Create a billing meter event</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/meters</h2>
        <p>List billing meters</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Filter results to only include meters with the given status.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meters</h2>
        <p>Create a billing meter</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/meters/{id}</h2>
        <p>Retrieve a billing meter</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meters/{id}</h2>
        <p>Update a billing meter</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meters/{id}/deactivate</h2>
        <p>Deactivate a billing meter</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing/meters/{id}/event_summaries</h2>
        <p>List billing meter event summaries</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): The customer for which to fetch event summaries.</li>

            <li>end_time (query): The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): Unique identifier for the object.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>start_time (query): The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>value_grouping_window (query): Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing/meters/{id}/reactivate</h2>
        <p>Reactivate a billing meter</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): Unique identifier for the object.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing_portal/configurations</h2>
        <p>List portal configurations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations).</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>is_default (query): Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration).</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing_portal/configurations</h2>
        <p>Create a portal configuration</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/billing_portal/configurations/{configuration}</h2>
        <p>Retrieve a portal configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing_portal/configurations/{configuration}</h2>
        <p>Update a portal configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/billing_portal/sessions</h2>
        <p>Create a portal session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges</h2>
        <p>List all charges</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return charges that were created during the given date interval.</li>

            <li>customer (query): Only return charges for the customer specified by this customer ID.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_intent (query): Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>transfer_group (query): Only return charges for this transfer group, limited to 100.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges</h2>
        <p>No summary available. (AI failed)</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges/search</h2>
        <p>Search charges</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges/{charge}</h2>
        <p>Retrieve a charge</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}</h2>
        <p>Update a charge</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/capture</h2>
        <p>Capture a payment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges/{charge}/dispute</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/dispute</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/dispute/close</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/refund</h2>
        <p>Create a refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): The identifier of the charge to refund.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges/{charge}/refunds</h2>
        <p>List all refunds</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/refunds</h2>
        <p>Create customer balance refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): The identifier of the charge to refund.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/charges/{charge}/refunds/{refund}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/charges/{charge}/refunds/{refund}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (path): </li>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/checkout/sessions</h2>
        <p>List all Checkout Sessions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return Checkout Sessions that were created during the given date interval.</li>

            <li>customer (query): Only return the Checkout Sessions for the Customer specified.</li>

            <li>customer_details (query): Only return the Checkout Sessions for the Customer details specified.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_intent (query): Only return the Checkout Session for the PaymentIntent specified.</li>

            <li>payment_link (query): Only return the Checkout Sessions for the Payment Link specified.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return the Checkout Sessions matching the given status.</li>

            <li>subscription (query): Only return the Checkout Session for the subscription specified.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/checkout/sessions</h2>
        <p>Create a Checkout Session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/checkout/sessions/{session}</h2>
        <p>Retrieve a Checkout Session</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/checkout/sessions/{session}</h2>
        <p>Update a Checkout Session</p>


        <h3>Parameters:</h3>
        <ul>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/checkout/sessions/{session}/expire</h2>
        <p>Expire a Checkout Session</p>


        <h3>Parameters:</h3>
        <ul>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/checkout/sessions/{session}/line_items</h2>
        <p>Retrieve a Checkout Session's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>session (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/orders</h2>
        <p>List orders</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/climate/orders</h2>
        <p>Create an order</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/orders/{order}</h2>
        <p>Retrieve an order</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>order (path): Unique identifier of the order.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/climate/orders/{order}</h2>
        <p>Update an order</p>


        <h3>Parameters:</h3>
        <ul>

            <li>order (path): Unique identifier of the order.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/climate/orders/{order}/cancel</h2>
        <p>Cancel an order</p>


        <h3>Parameters:</h3>
        <ul>

            <li>order (path): Unique identifier of the order.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/products</h2>
        <p>List products</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/products/{product}</h2>
        <p>Retrieve a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>product (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/suppliers</h2>
        <p>List suppliers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/climate/suppliers/{supplier}</h2>
        <p>Retrieve a supplier</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>supplier (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/confirmation_tokens/{confirmation_token}</h2>
        <p>Retrieve a ConfirmationToken</p>


        <h3>Parameters:</h3>
        <ul>

            <li>confirmation_token (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/country_specs</h2>
        <p>List Country Specs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/country_specs/{country}</h2>
        <p>Retrieve a Country Spec</p>


        <h3>Parameters:</h3>
        <ul>

            <li>country (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/coupons</h2>
        <p>List all coupons</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/coupons</h2>
        <p>Create a coupon</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/coupons/{coupon}</h2>
        <p>Delete a coupon</p>


        <h3>Parameters:</h3>
        <ul>

            <li>coupon (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/coupons/{coupon}</h2>
        <p>Retrieve a coupon</p>


        <h3>Parameters:</h3>
        <ul>

            <li>coupon (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/coupons/{coupon}</h2>
        <p>Update a coupon</p>


        <h3>Parameters:</h3>
        <ul>

            <li>coupon (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/credit_notes</h2>
        <p>List all credit notes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return credit notes that were created during the given date interval.</li>

            <li>customer (query): Only return credit notes for the customer specified by this customer ID.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (query): Only return credit notes for the invoice specified by this invoice ID.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/credit_notes</h2>
        <p>Create a credit note</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/credit_notes/preview</h2>
        <p>Preview a credit note</p>


        <h3>Parameters:</h3>
        <ul>

            <li>amount (query): The integer amount in cents (or local equivalent) representing the total amount of the credit note.</li>

            <li>credit_amount (query): The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.</li>

            <li>effective_at (query): The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.</li>

            <li>email_type (query): Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (query): ID of the invoice.</li>

            <li>lines (query): Line items that make up the credit note.</li>

            <li>memo (query): The credit note's memo appears on the credit note PDF.</li>

            <li>metadata (query): Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.</li>

            <li>out_of_band_amount (query): The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.</li>

            <li>reason (query): Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`</li>

            <li>refund_amount (query): The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.</li>

            <li>refunds (query): Refunds to link to this credit note.</li>

            <li>shipping_cost (query): When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/credit_notes/preview/lines</h2>
        <p>Retrieve a credit note preview's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>amount (query): The integer amount in cents (or local equivalent) representing the total amount of the credit note.</li>

            <li>credit_amount (query): The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.</li>

            <li>effective_at (query): The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.</li>

            <li>email_type (query): Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (query): ID of the invoice.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>lines (query): Line items that make up the credit note.</li>

            <li>memo (query): The credit note's memo appears on the credit note PDF.</li>

            <li>metadata (query): Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.</li>

            <li>out_of_band_amount (query): The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.</li>

            <li>reason (query): Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`</li>

            <li>refund_amount (query): The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.</li>

            <li>refunds (query): Refunds to link to this credit note.</li>

            <li>shipping_cost (query): When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/credit_notes/{credit_note}/lines</h2>
        <p>Retrieve a credit note's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>credit_note (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/credit_notes/{id}</h2>
        <p>Retrieve a credit note</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/credit_notes/{id}</h2>
        <p>Update a credit note</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/credit_notes/{id}/void</h2>
        <p>Void a credit note</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customer_sessions</h2>
        <p>Create a Customer Session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers</h2>
        <p>List all customers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return customers that were created during the given date interval.</li>

            <li>email (query): A case-sensitive filter on the list based on the customer's `email` field. The value must be a string.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>test_clock (query): Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers</h2>
        <p>Create a customer</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/search</h2>
        <p>Search customers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}</h2>
        <p>Delete a customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}</h2>
        <p>Retrieve a customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}</h2>
        <p>Update a customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/balance_transactions</h2>
        <p>List customer balance transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/balance_transactions</h2>
        <p>Create a customer balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/balance_transactions/{transaction}</h2>
        <p>Retrieve a customer balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/balance_transactions/{transaction}</h2>
        <p>Update a customer credit balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/bank_accounts</h2>
        <p>List all bank accounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/bank_accounts</h2>
        <p>Create a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/bank_accounts/{id}</h2>
        <p>Delete a customer source</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/bank_accounts/{id}</h2>
        <p>Retrieve a bank account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/bank_accounts/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/bank_accounts/{id}/verify</h2>
        <p>Verify a bank account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/cards</h2>
        <p>List all cards</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/cards</h2>
        <p>Create a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/cards/{id}</h2>
        <p>Delete a customer source</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/cards/{id}</h2>
        <p>Retrieve a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/cards/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/cash_balance</h2>
        <p>Retrieve a cash balance</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/cash_balance</h2>
        <p>Update a cash balance's settings</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/cash_balance_transactions</h2>
        <p>List cash balance transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/cash_balance_transactions/{transaction}</h2>
        <p>Retrieve a cash balance transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/discount</h2>
        <p>Delete a customer discount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/discount</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/funding_instructions</h2>
        <p>Create or retrieve funding instructions for a customer cash balance</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/payment_methods</h2>
        <p>List a Customer's PaymentMethods</p>


        <h3>Parameters:</h3>
        <ul>

            <li>allow_redisplay (query): This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.</li>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/payment_methods/{payment_method}</h2>
        <p>Retrieve a Customer's PaymentMethod</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>payment_method (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/sources</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>object (query): Filter sources according to a particular object type.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/sources</h2>
        <p>Create a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/sources/{id}</h2>
        <p>Delete a customer source</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/sources/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/sources/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/sources/{id}/verify</h2>
        <p>Verify a bank account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/subscriptions</h2>
        <p>List active subscriptions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/subscriptions</h2>
        <p>Create a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/subscriptions/{subscription_exposed_id}</h2>
        <p>Cancel a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/subscriptions/{subscription_exposed_id}</h2>
        <p>Retrieve a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/subscriptions/{subscription_exposed_id}</h2>
        <p>Update a subscription on a customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount</h2>
        <p>Delete a customer discount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/tax_ids</h2>
        <p>List all Customer tax IDs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/customers/{customer}/tax_ids</h2>
        <p>Create a Customer tax ID</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/customers/{customer}/tax_ids/{id}</h2>
        <p>Delete a Customer tax ID</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/customers/{customer}/tax_ids/{id}</h2>
        <p>Retrieve a Customer tax ID</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/disputes</h2>
        <p>List all disputes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (query): Only return disputes associated to the charge specified by this charge ID.</li>

            <li>created (query): Only return disputes that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_intent (query): Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/disputes/{dispute}</h2>
        <p>Retrieve a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/disputes/{dispute}</h2>
        <p>Update a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/disputes/{dispute}/close</h2>
        <p>Close a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/entitlements/active_entitlements</h2>
        <p>List all active entitlements</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): The ID of the customer.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/entitlements/active_entitlements/{id}</h2>
        <p>Retrieve an active entitlement</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): The ID of the entitlement.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/entitlements/features</h2>
        <p>List all features</p>


        <h3>Parameters:</h3>
        <ul>

            <li>archived (query): If set, filter results to only include features with the given archive status.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>lookup_key (query): If set, filter results to only include features with the given lookup_key.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/entitlements/features</h2>
        <p>Create a feature</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/entitlements/features/{id}</h2>
        <p>Retrieve a feature</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): The ID of the feature.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/entitlements/features/{id}</h2>
        <p>Updates a feature</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/ephemeral_keys</h2>
        <p>Create an ephemeral key</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/ephemeral_keys/{key}</h2>
        <p>Immediately invalidate an ephemeral key</p>


        <h3>Parameters:</h3>
        <ul>

            <li>key (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/events</h2>
        <p>List all events</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return events that were created during the given date interval.</li>

            <li>delivery_success (query): Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property.</li>

            <li>types (query): An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/events/{id}</h2>
        <p>Retrieve an event</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/exchange_rates</h2>
        <p>List all exchange rates</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with the exchange rate for currency X your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and total number of supported payout currencies, and the default is the max.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with the exchange rate for currency X, your subsequent call can include `starting_after=X` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/exchange_rates/{rate_id}</h2>
        <p>Retrieve an exchange rate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>rate_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/external_accounts/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/file_links</h2>
        <p>List all file links</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return links that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>expired (query): Filter links by their expiration status. By default, Stripe returns all links.</li>

            <li>file (query): Only return links for the given file.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/file_links</h2>
        <p>Create a file link</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/file_links/{link}</h2>
        <p>Retrieve a file link</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>link (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/file_links/{link}</h2>
        <p>Update a file link</p>


        <h3>Parameters:</h3>
        <ul>

            <li>link (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/files</h2>
        <p>List all files</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return files that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>purpose (query): Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/files</h2>
        <p>Create a file</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/files/{file}</h2>
        <p>Retrieve a file</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>file (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/accounts</h2>
        <p>List Accounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account_holder (query): If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>session (query): If present, only return accounts that were collected as part of the given session.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/accounts/{account}</h2>
        <p>Retrieve an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/financial_connections/accounts/{account}/disconnect</h2>
        <p>Disconnect an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/accounts/{account}/owners</h2>
        <p>List Account Owners</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>ownership (query): The ID of the ownership object to fetch owners from.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/financial_connections/accounts/{account}/refresh</h2>
        <p>Refresh Account data</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/financial_connections/accounts/{account}/subscribe</h2>
        <p>Subscribe to data refreshes for an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/financial_connections/accounts/{account}/unsubscribe</h2>
        <p>Unsubscribe from data refreshes for an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/financial_connections/sessions</h2>
        <p>Create a Session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/sessions/{session}</h2>
        <p>Retrieve a Session</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/transactions</h2>
        <p>List Transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (query): The ID of the Financial Connections Account whose transactions will be retrieved.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>transacted_at (query): A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:</li>

            <li>transaction_refresh (query): A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/financial_connections/transactions/{transaction}</h2>
        <p>Retrieve a Transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/forwarding/requests</h2>
        <p>List all ForwardingRequests</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.</li>

            <li>ending_before (query): A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/forwarding/requests</h2>
        <p>Create a ForwardingRequest</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/forwarding/requests/{id}</h2>
        <p>Retrieve a ForwardingRequest</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/identity/verification_reports</h2>
        <p>List VerificationReports</p>


        <h3>Parameters:</h3>
        <ul>

            <li>client_reference_id (query): A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.</li>

            <li>created (query): Only return VerificationReports that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): Only return VerificationReports of this type</li>

            <li>verification_session (query): Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/identity/verification_reports/{report}</h2>
        <p>Retrieve a VerificationReport</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>report (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/identity/verification_sessions</h2>
        <p>List VerificationSessions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>client_reference_id (query): A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.</li>

            <li>created (query): Only return VerificationSessions that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>related_customer (query): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/identity/verification_sessions</h2>
        <p>Create a VerificationSession</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/identity/verification_sessions/{session}</h2>
        <p>Retrieve a VerificationSession</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/identity/verification_sessions/{session}</h2>
        <p>Update a VerificationSession</p>


        <h3>Parameters:</h3>
        <ul>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/identity/verification_sessions/{session}/cancel</h2>
        <p>Cancel a VerificationSession</p>


        <h3>Parameters:</h3>
        <ul>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/identity/verification_sessions/{session}/redact</h2>
        <p>Redact a VerificationSession</p>


        <h3>Parameters:</h3>
        <ul>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoice_payments</h2>
        <p>List all payments for an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (query): The identifier of the invoice whose payments to return.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment (query): The payment details of the invoice payments to return.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): The status of the invoice payments to return.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoice_payments/{invoice_payment}</h2>
        <p>Retrieve an InvoicePayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice_payment (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoice_rendering_templates</h2>
        <p>List all invoice rendering templates</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoice_rendering_templates/{template}</h2>
        <p>Retrieve an invoice rendering template</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>template (path): </li>

            <li>version (query): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoice_rendering_templates/{template}/archive</h2>
        <p>Archive an invoice rendering template</p>


        <h3>Parameters:</h3>
        <ul>

            <li>template (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoice_rendering_templates/{template}/unarchive</h2>
        <p>Unarchive an invoice rendering template</p>


        <h3>Parameters:</h3>
        <ul>

            <li>template (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoiceitems</h2>
        <p>List all invoice items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return invoice items that were created during the given date interval.</li>

            <li>customer (query): The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (query): Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>pending (query): Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoiceitems</h2>
        <p>Create an invoice item</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/invoiceitems/{invoiceitem}</h2>
        <p>Delete an invoice item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoiceitem (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoiceitems/{invoiceitem}</h2>
        <p>Retrieve an invoice item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoiceitem (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoiceitems/{invoiceitem}</h2>
        <p>Update an invoice item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoiceitem (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoices</h2>
        <p>List all invoices</p>


        <h3>Parameters:</h3>
        <ul>

            <li>collection_method (query): The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.</li>

            <li>created (query): Only return invoices that were created during the given date interval.</li>

            <li>customer (query): Only return invoices for the customer specified by this customer ID.</li>

            <li>due_date (query): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)</li>

            <li>subscription (query): Only return invoices for the subscription specified by this subscription ID.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices</h2>
        <p>Create an invoice</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/create_preview</h2>
        <p>Create a preview invoice</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoices/search</h2>
        <p>Search invoices</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/invoices/{invoice}</h2>
        <p>Delete a draft invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoices/{invoice}</h2>
        <p>Retrieve an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}</h2>
        <p>Update an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/add_lines</h2>
        <p>Bulk add invoice line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/finalize</h2>
        <p>Finalize an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/invoices/{invoice}/lines</h2>
        <p>Retrieve an invoice's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>invoice (path): </li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/lines/{line_item_id}</h2>
        <p>Update an invoice's line item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): Invoice ID of line item</li>

            <li>line_item_id (path): Invoice line item ID</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/mark_uncollectible</h2>
        <p>Mark an invoice as uncollectible</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/pay</h2>
        <p>Pay an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/remove_lines</h2>
        <p>Bulk remove invoice line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/send</h2>
        <p>Send an invoice for manual payment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/update_lines</h2>
        <p>Bulk update invoice line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/invoices/{invoice}/void</h2>
        <p>Void an invoice</p>


        <h3>Parameters:</h3>
        <ul>

            <li>invoice (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/authorizations</h2>
        <p>List all authorizations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (query): Only return authorizations that belong to the given card.</li>

            <li>cardholder (query): Only return authorizations that belong to the given cardholder.</li>

            <li>created (query): Only return authorizations that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/authorizations/{authorization}</h2>
        <p>Retrieve an authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/authorizations/{authorization}</h2>
        <p>Update an authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/authorizations/{authorization}/approve</h2>
        <p>Approve an authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/authorizations/{authorization}/decline</h2>
        <p>Decline an authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/cardholders</h2>
        <p>List all cardholders</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return cardholders that were created during the given date interval.</li>

            <li>email (query): Only return cardholders that have the given email address.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>phone_number (query): Only return cardholders that have the given phone number.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`.</li>

            <li>type (query): Only return cardholders that have the given type. One of `individual` or `company`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/cardholders</h2>
        <p>Create a cardholder</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/cardholders/{cardholder}</h2>
        <p>Retrieve a cardholder</p>


        <h3>Parameters:</h3>
        <ul>

            <li>cardholder (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/cardholders/{cardholder}</h2>
        <p>Update a cardholder</p>


        <h3>Parameters:</h3>
        <ul>

            <li>cardholder (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/cards</h2>
        <p>List all cards</p>


        <h3>Parameters:</h3>
        <ul>

            <li>cardholder (query): Only return cards belonging to the Cardholder with the provided ID.</li>

            <li>created (query): Only return cards that were issued during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>exp_month (query): Only return cards that have the given expiration month.</li>

            <li>exp_year (query): Only return cards that have the given expiration year.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>last4 (query): Only return cards that have the given last four digits.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>personalization_design (query): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.</li>

            <li>type (query): Only return cards that have the given type. One of `virtual` or `physical`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/cards</h2>
        <p>Create a card</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/cards/{card}</h2>
        <p>Retrieve a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/cards/{card}</h2>
        <p>Update a card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/disputes</h2>
        <p>List all disputes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return Issuing disputes that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Select Issuing disputes with the given status.</li>

            <li>transaction (query): Select the Issuing dispute for the given transaction.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/disputes</h2>
        <p>Create a dispute</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/disputes/{dispute}</h2>
        <p>Retrieve a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/disputes/{dispute}</h2>
        <p>Update a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/disputes/{dispute}/submit</h2>
        <p>Submit a dispute</p>


        <h3>Parameters:</h3>
        <ul>

            <li>dispute (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/personalization_designs</h2>
        <p>List all personalization designs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>lookup_keys (query): Only return personalization designs with the given lookup keys.</li>

            <li>preferences (query): Only return personalization designs with the given preferences.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return personalization designs with the given status.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/personalization_designs</h2>
        <p>Create a personalization design</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/personalization_designs/{personalization_design}</h2>
        <p>Retrieve a personalization design</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>personalization_design (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/personalization_designs/{personalization_design}</h2>
        <p>Update a personalization design</p>


        <h3>Parameters:</h3>
        <ul>

            <li>personalization_design (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/physical_bundles</h2>
        <p>List all physical bundles</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return physical bundles with the given status.</li>

            <li>type (query): Only return physical bundles with the given type.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/physical_bundles/{physical_bundle}</h2>
        <p>Retrieve a physical bundle</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>physical_bundle (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/settlements/{settlement}</h2>
        <p>Retrieve a settlement</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>settlement (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/settlements/{settlement}</h2>
        <p>Update a settlement</p>


        <h3>Parameters:</h3>
        <ul>

            <li>settlement (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/tokens</h2>
        <p>List all issuing tokens for card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (query): The Issuing card identifier to list tokens for.</li>

            <li>created (query): Only return Issuing tokens that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Select Issuing tokens with the given status.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/tokens/{token}</h2>
        <p>Retrieve an issuing token</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>token (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/tokens/{token}</h2>
        <p>Update a token status</p>


        <h3>Parameters:</h3>
        <ul>

            <li>token (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/transactions</h2>
        <p>List all transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (query): Only return transactions that belong to the given card.</li>

            <li>cardholder (query): Only return transactions that belong to the given cardholder.</li>

            <li>created (query): Only return transactions that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): Only return transactions that have the given type. One of `capture` or `refund`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/issuing/transactions/{transaction}</h2>
        <p>Retrieve a transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/issuing/transactions/{transaction}</h2>
        <p>Update a transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/link_account_sessions</h2>
        <p>Create a Session</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/link_account_sessions/{session}</h2>
        <p>Retrieve a Session</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>session (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/linked_accounts</h2>
        <p>List Accounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account_holder (query): If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>session (query): If present, only return accounts that were collected as part of the given session.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/linked_accounts/{account}</h2>
        <p>Retrieve an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/linked_accounts/{account}/disconnect</h2>
        <p>Disconnect an Account</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/linked_accounts/{account}/owners</h2>
        <p>List Account Owners</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>ownership (query): The ID of the ownership object to fetch owners from.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/linked_accounts/{account}/refresh</h2>
        <p>Refresh Account data</p>


        <h3>Parameters:</h3>
        <ul>

            <li>account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/mandates/{mandate}</h2>
        <p>Retrieve a Mandate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>mandate (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_intents</h2>
        <p>List all PaymentIntents</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options.</li>

            <li>customer (query): Only return PaymentIntents for the customer that this customer ID specifies.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents</h2>
        <p>Create a PaymentIntent</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_intents/search</h2>
        <p>Search PaymentIntents</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_intents/{intent}</h2>
        <p>Retrieve a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>client_secret (query): The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}</h2>
        <p>Update a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/apply_customer_balance</h2>
        <p>Reconcile a customer_balance PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/cancel</h2>
        <p>Cancel a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/capture</h2>
        <p>Capture a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/confirm</h2>
        <p>Confirm a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/increment_authorization</h2>
        <p>Increment an authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_intents/{intent}/verify_microdeposits</h2>
        <p>Verify microdeposits on a PaymentIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_links</h2>
        <p>List all payment links</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_links</h2>
        <p>Create a payment link</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_links/{payment_link}</h2>
        <p>Retrieve payment link</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>payment_link (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_links/{payment_link}</h2>
        <p>Update a payment link</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_link (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_links/{payment_link}/line_items</h2>
        <p>Retrieve a payment link's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_link (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_method_configurations</h2>
        <p>List payment method configurations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>application (query): The Connect application to filter by.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_method_configurations</h2>
        <p>Create a payment method configuration</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_method_configurations/{configuration}</h2>
        <p>Retrieve payment method configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_method_configurations/{configuration}</h2>
        <p>Update payment method configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_method_domains</h2>
        <p>List payment method domains</p>


        <h3>Parameters:</h3>
        <ul>

            <li>domain_name (query): The domain name that this payment method domain object represents.</li>

            <li>enabled (query): Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_method_domains</h2>
        <p>Create a payment method domain</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_method_domains/{payment_method_domain}</h2>
        <p>Retrieve a payment method domain</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>payment_method_domain (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_method_domains/{payment_method_domain}</h2>
        <p>Update a payment method domain</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_method_domain (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_method_domains/{payment_method_domain}/validate</h2>
        <p>Validate an existing payment method domain</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_method_domain (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_methods</h2>
        <p>List PaymentMethods</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): The ID of the customer whose PaymentMethods will be retrieved.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_methods</h2>
        <p>Shares a PaymentMethod</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payment_methods/{payment_method}</h2>
        <p>Retrieve a PaymentMethod</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>payment_method (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_methods/{payment_method}</h2>
        <p>Update a PaymentMethod</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_method (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_methods/{payment_method}/attach</h2>
        <p>Attach a PaymentMethod to a Customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_method (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payment_methods/{payment_method}/detach</h2>
        <p>Detach a PaymentMethod from a Customer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payment_method (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payouts</h2>
        <p>List all payouts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>arrival_date (query): Only return payouts that are expected to arrive during the given date interval.</li>

            <li>created (query): Only return payouts that were created during the given date interval.</li>

            <li>destination (query): The ID of an external account - only return payouts sent to this external account.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payouts</h2>
        <p>Create a payout</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/payouts/{payout}</h2>
        <p>Retrieve a payout</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>payout (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payouts/{payout}</h2>
        <p>Update a payout</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payout (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payouts/{payout}/cancel</h2>
        <p>Cancel a payout</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payout (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/payouts/{payout}/reverse</h2>
        <p>Reverse a payout</p>


        <h3>Parameters:</h3>
        <ul>

            <li>payout (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/plans</h2>
        <p>List all plans</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>product (query): Only return plans for the given product.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/plans</h2>
        <p>Create a plan</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/plans/{plan}</h2>
        <p>Delete a plan</p>


        <h3>Parameters:</h3>
        <ul>

            <li>plan (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/plans/{plan}</h2>
        <p>Retrieve a plan</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>plan (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/plans/{plan}</h2>
        <p>Update a plan</p>


        <h3>Parameters:</h3>
        <ul>

            <li>plan (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/prices</h2>
        <p>List all prices</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices).</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>currency (query): Only return prices for the given currency.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>lookup_keys (query): Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.</li>

            <li>product (query): Only return prices for the given product.</li>

            <li>recurring (query): Only return prices with these recurring fields.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>type (query): Only return prices of type `recurring` or `one_time`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/prices</h2>
        <p>Create a price</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/prices/search</h2>
        <p>Search prices</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/prices/{price}</h2>
        <p>Retrieve a price</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>price (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/prices/{price}</h2>
        <p>Update a price</p>


        <h3>Parameters:</h3>
        <ul>

            <li>price (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/products</h2>
        <p>List all products</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return products that are active or inactive (e.g., pass `false` to list all inactive products).</li>

            <li>created (query): Only return products that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>ids (query): Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before).</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>shippable (query): Only return products that can be shipped (i.e., physical, not digital products).</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>url (query): Only return products with the given url.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/products</h2>
        <p>Create a product</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/products/search</h2>
        <p>Search products</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/products/{id}</h2>
        <p>Delete a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/products/{id}</h2>
        <p>Retrieve a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/products/{id}</h2>
        <p>Update a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/products/{product}/features</h2>
        <p>List all features attached to a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>product (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/products/{product}/features</h2>
        <p>Attach a feature to a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>product (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/products/{product}/features/{id}</h2>
        <p>Remove a feature from a product</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

            <li>product (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/products/{product}/features/{id}</h2>
        <p>Retrieve a product_feature</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): The ID of the product_feature.</li>

            <li>product (path): The ID of the product.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/promotion_codes</h2>
        <p>List all promotion codes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Filter promotion codes by whether they are active.</li>

            <li>code (query): Only return promotion codes that have this case-insensitive code.</li>

            <li>coupon (query): Only return promotion codes for this coupon.</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>customer (query): Only return promotion codes that are restricted to this customer.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/promotion_codes</h2>
        <p>Create a promotion code</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/promotion_codes/{promotion_code}</h2>
        <p>Retrieve a promotion code</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>promotion_code (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/promotion_codes/{promotion_code}</h2>
        <p>Update a promotion code</p>


        <h3>Parameters:</h3>
        <ul>

            <li>promotion_code (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/quotes</h2>
        <p>List all quotes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (query): The ID of the customer whose quotes will be retrieved.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): The status of the quote.</li>

            <li>test_clock (query): Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/quotes</h2>
        <p>Create a quote</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/quotes/{quote}</h2>
        <p>Retrieve a quote</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/quotes/{quote}</h2>
        <p>Update a quote</p>


        <h3>Parameters:</h3>
        <ul>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/quotes/{quote}/accept</h2>
        <p>Accept a quote</p>


        <h3>Parameters:</h3>
        <ul>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/quotes/{quote}/cancel</h2>
        <p>Cancel a quote</p>


        <h3>Parameters:</h3>
        <ul>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/quotes/{quote}/computed_upfront_line_items</h2>
        <p>Retrieve a quote's upfront line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>quote (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/quotes/{quote}/finalize</h2>
        <p>Finalize a quote</p>


        <h3>Parameters:</h3>
        <ul>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/quotes/{quote}/line_items</h2>
        <p>Retrieve a quote's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>quote (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/quotes/{quote}/pdf</h2>
        <p>Download quote PDF</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>quote (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/early_fraud_warnings</h2>
        <p>List all early fraud warnings</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (query): Only return early fraud warnings for the charge specified by this charge ID.</li>

            <li>created (query): Only return early fraud warnings that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_intent (query): Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/early_fraud_warnings/{early_fraud_warning}</h2>
        <p>Retrieve an early fraud warning</p>


        <h3>Parameters:</h3>
        <ul>

            <li>early_fraud_warning (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/value_list_items</h2>
        <p>List all value list items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return items that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>value (query): Return items belonging to the parent list whose value matches the specified value (using an "is like" match).</li>

            <li>value_list (query): Identifier for the parent value list this item belongs to.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/radar/value_list_items</h2>
        <p>Create a value list item</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/radar/value_list_items/{item}</h2>
        <p>Delete a value list item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>item (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/value_list_items/{item}</h2>
        <p>Retrieve a value list item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>item (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/value_lists</h2>
        <p>List all value lists</p>


        <h3>Parameters:</h3>
        <ul>

            <li>alias (query): The alias used to reference the value list when writing rules.</li>

            <li>contains (query): A value contained within a value list - returns all value lists containing this value.</li>

            <li>created (query): Only return value lists that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/radar/value_lists</h2>
        <p>Create a value list</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/radar/value_lists/{value_list}</h2>
        <p>Delete a value list</p>


        <h3>Parameters:</h3>
        <ul>

            <li>value_list (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/radar/value_lists/{value_list}</h2>
        <p>Retrieve a value list</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>value_list (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/radar/value_lists/{value_list}</h2>
        <p>Update a value list</p>


        <h3>Parameters:</h3>
        <ul>

            <li>value_list (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/refunds</h2>
        <p>List all refunds</p>


        <h3>Parameters:</h3>
        <ul>

            <li>charge (query): Only return refunds for the charge specified by this charge ID.</li>

            <li>created (query): Only return refunds that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_intent (query): Only return refunds for the PaymentIntent specified by this ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/refunds</h2>
        <p>Create customer balance refund</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/refunds/{refund}</h2>
        <p>Retrieve a refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/refunds/{refund}</h2>
        <p>Update a refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/refunds/{refund}/cancel</h2>
        <p>Cancel a refund</p>


        <h3>Parameters:</h3>
        <ul>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reporting/report_runs</h2>
        <p>List all Report Runs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return Report Runs that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/reporting/report_runs</h2>
        <p>Create a Report Run</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reporting/report_runs/{report_run}</h2>
        <p>Retrieve a Report Run</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>report_run (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reporting/report_types</h2>
        <p>List all Report Types</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reporting/report_types/{report_type}</h2>
        <p>Retrieve a Report Type</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>report_type (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reviews</h2>
        <p>List all open reviews</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return reviews that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/reviews/{review}</h2>
        <p>Retrieve a review</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>review (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/reviews/{review}/approve</h2>
        <p>Approve a review</p>


        <h3>Parameters:</h3>
        <ul>

            <li>review (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/setup_attempts</h2>
        <p>List all SetupAttempts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): A filter on the list, based on the object `created` field. The value
can be a string with an integer Unix timestamp or a
dictionary with a number of different query options.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>setup_intent (query): Only return SetupAttempts created by the SetupIntent specified by
this ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/setup_intents</h2>
        <p>List all SetupIntents</p>


        <h3>Parameters:</h3>
        <ul>

            <li>attach_to_self (query): If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>customer (query): Only return SetupIntents for the customer specified by this customer ID.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>payment_method (query): Only return SetupIntents that associate with the specified payment method.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/setup_intents</h2>
        <p>Create a SetupIntent</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/setup_intents/{intent}</h2>
        <p>Retrieve a SetupIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>client_secret (query): The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/setup_intents/{intent}</h2>
        <p>Update a SetupIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/setup_intents/{intent}/cancel</h2>
        <p>Cancel a SetupIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/setup_intents/{intent}/confirm</h2>
        <p>Confirm a SetupIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/setup_intents/{intent}/verify_microdeposits</h2>
        <p>Verify microdeposits on a SetupIntent</p>


        <h3>Parameters:</h3>
        <ul>

            <li>intent (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/shipping_rates</h2>
        <p>List all shipping rates</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Only return shipping rates that are active or inactive.</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>currency (query): Only return shipping rates for the given currency.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/shipping_rates</h2>
        <p>Create a shipping rate</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/shipping_rates/{shipping_rate_token}</h2>
        <p>Retrieve a shipping rate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>shipping_rate_token (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/shipping_rates/{shipping_rate_token}</h2>
        <p>Update a shipping rate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>shipping_rate_token (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/sigma/saved_queries/{id}</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sigma/scheduled_query_runs</h2>
        <p>List all scheduled query runs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sigma/scheduled_query_runs/{scheduled_query_run}</h2>
        <p>Retrieve a scheduled query run</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>scheduled_query_run (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/sources</h2>
        <p>Shares a source</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sources/{source}</h2>
        <p>Retrieve a source</p>


        <h3>Parameters:</h3>
        <ul>

            <li>client_secret (query): The client secret of the source. Required if a publishable key is used to retrieve the source.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>source (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/sources/{source}</h2>
        <p>Update a source</p>


        <h3>Parameters:</h3>
        <ul>

            <li>source (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sources/{source}/mandate_notifications/{mandate_notification}</h2>
        <p>Retrieve a Source MandateNotification</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>mandate_notification (path): </li>

            <li>source (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sources/{source}/source_transactions</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>source (path): </li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/sources/{source}/source_transactions/{source_transaction}</h2>
        <p>Retrieve a source transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>source (path): </li>

            <li>source_transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/sources/{source}/verify</h2>
        <p>No summary available. (AI failed)</p>


        <h3>Parameters:</h3>
        <ul>

            <li>source (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscription_items</h2>
        <p>List all subscription items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>subscription (query): The ID of the subscription whose items will be retrieved.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_items</h2>
        <p>Create a subscription item</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/subscription_items/{item}</h2>
        <p>Delete a subscription item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>item (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscription_items/{item}</h2>
        <p>Retrieve a subscription item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>item (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_items/{item}</h2>
        <p>Update a subscription item</p>


        <h3>Parameters:</h3>
        <ul>

            <li>item (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscription_schedules</h2>
        <p>List all schedules</p>


        <h3>Parameters:</h3>
        <ul>

            <li>canceled_at (query): Only return subscription schedules that were created canceled the given date interval.</li>

            <li>completed_at (query): Only return subscription schedules that completed during the given date interval.</li>

            <li>created (query): Only return subscription schedules that were created during the given date interval.</li>

            <li>customer (query): Only return subscription schedules for the given customer.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>released_at (query): Only return subscription schedules that were released during the given date interval.</li>

            <li>scheduled (query): Only return subscription schedules that have not started yet.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_schedules</h2>
        <p>Create a schedule</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscription_schedules/{schedule}</h2>
        <p>Retrieve a schedule</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>schedule (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_schedules/{schedule}</h2>
        <p>Update a schedule</p>


        <h3>Parameters:</h3>
        <ul>

            <li>schedule (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_schedules/{schedule}/cancel</h2>
        <p>Cancel a schedule</p>


        <h3>Parameters:</h3>
        <ul>

            <li>schedule (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscription_schedules/{schedule}/release</h2>
        <p>Release a schedule</p>


        <h3>Parameters:</h3>
        <ul>

            <li>schedule (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscriptions</h2>
        <p>List subscriptions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>automatic_tax (query): Filter subscriptions by their automatic tax settings.</li>

            <li>collection_method (query): The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.</li>

            <li>created (query): Only return subscriptions that were created during the given date interval.</li>

            <li>current_period_end (query): Only return subscriptions whose current_period_end falls within the given date interval.</li>

            <li>current_period_start (query): Only return subscriptions whose current_period_start falls within the given date interval.</li>

            <li>customer (query): The ID of the customer whose subscriptions will be retrieved.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>price (query): Filter for subscriptions that contain this recurring price ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.</li>

            <li>test_clock (query): Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscriptions</h2>
        <p>Create a subscription</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscriptions/search</h2>
        <p>Search subscriptions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>page (query): A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.</li>

            <li>query (query): The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions).</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/subscriptions/{subscription_exposed_id}</h2>
        <p>Cancel a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/subscriptions/{subscription_exposed_id}</h2>
        <p>Retrieve a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscriptions/{subscription_exposed_id}</h2>
        <p>Update a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/subscriptions/{subscription_exposed_id}/discount</h2>
        <p>Delete a subscription discount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>subscription_exposed_id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/subscriptions/{subscription}/resume</h2>
        <p>Resume a subscription</p>


        <h3>Parameters:</h3>
        <ul>

            <li>subscription (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/calculations</h2>
        <p>Create a Tax Calculation</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/calculations/{calculation}</h2>
        <p>Retrieve a Tax Calculation</p>


        <h3>Parameters:</h3>
        <ul>

            <li>calculation (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/calculations/{calculation}/line_items</h2>
        <p>Retrieve a calculation's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>calculation (path): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/registrations</h2>
        <p>List registrations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): The status of the Tax Registration.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/registrations</h2>
        <p>Create a registration</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/registrations/{id}</h2>
        <p>Retrieve a registration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/registrations/{id}</h2>
        <p>Update a registration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/settings</h2>
        <p>Retrieve settings</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/settings</h2>
        <p>Update settings</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/transactions/create_from_calculation</h2>
        <p>Create a transaction from a calculation</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax/transactions/create_reversal</h2>
        <p>Create a reversal transaction</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/transactions/{transaction}</h2>
        <p>Retrieve a transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax/transactions/{transaction}/line_items</h2>
        <p>Retrieve a transaction's line items</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_codes</h2>
        <p>List all tax codes</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_codes/{id}</h2>
        <p>Retrieve a tax code</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_ids</h2>
        <p>List all tax IDs</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>owner (query): The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax_ids</h2>
        <p>Create a tax ID</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/tax_ids/{id}</h2>
        <p>Delete a tax ID</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_ids/{id}</h2>
        <p>Retrieve a tax ID</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_rates</h2>
        <p>List all tax rates</p>


        <h3>Parameters:</h3>
        <ul>

            <li>active (query): Optional flag to filter by tax rates that are either active or inactive (archived).</li>

            <li>created (query): Optional range for filtering created date.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>inclusive (query): Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax_rates</h2>
        <p>Create a tax rate</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tax_rates/{tax_rate}</h2>
        <p>Retrieve a tax rate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>tax_rate (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tax_rates/{tax_rate}</h2>
        <p>Update a tax rate</p>


        <h3>Parameters:</h3>
        <ul>

            <li>tax_rate (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/configurations</h2>
        <p>List all Configurations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>is_account_default (query): if present, only return the account default or non-default configurations.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/configurations</h2>
        <p>Create a Configuration</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/terminal/configurations/{configuration}</h2>
        <p>Delete a Configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/configurations/{configuration}</h2>
        <p>Retrieve a Configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/configurations/{configuration}</h2>
        <p>Update a Configuration</p>


        <h3>Parameters:</h3>
        <ul>

            <li>configuration (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/connection_tokens</h2>
        <p>Create a Connection Token</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/locations</h2>
        <p>List all Locations</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/locations</h2>
        <p>Create a Location</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/terminal/locations/{location}</h2>
        <p>Delete a Location</p>


        <h3>Parameters:</h3>
        <ul>

            <li>location (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/locations/{location}</h2>
        <p>Retrieve a Location</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>location (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/locations/{location}</h2>
        <p>Update a Location</p>


        <h3>Parameters:</h3>
        <ul>

            <li>location (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/readers</h2>
        <p>List all Readers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>device_type (query): Filters readers by device type</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>location (query): A location ID to filter the response list to only readers at the specific location</li>

            <li>serial_number (query): Filters readers by serial number</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): A status filter to filter readers to only offline or online readers</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers</h2>
        <p>Create a Reader</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/terminal/readers/{reader}</h2>
        <p>Delete a Reader</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/terminal/readers/{reader}</h2>
        <p>Retrieve a Reader</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}</h2>
        <p>Update a Reader</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}/cancel_action</h2>
        <p>Cancel the current reader action</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}/process_payment_intent</h2>
        <p>Hand-off a PaymentIntent to a Reader</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}/process_setup_intent</h2>
        <p>Hand-off a SetupIntent to a Reader</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}/refund_payment</h2>
        <p>Refund a Charge or a PaymentIntent in-person</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/terminal/readers/{reader}/set_reader_display</h2>
        <p>Set reader display</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/confirmation_tokens</h2>
        <p>Create a test Confirmation Token</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/customers/{customer}/fund_cash_balance</h2>
        <p>Fund a test mode cash balance</p>


        <h3>Parameters:</h3>
        <ul>

            <li>customer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations</h2>
        <p>Create a test-mode authorization</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/capture</h2>
        <p>Capture a test-mode authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/expire</h2>
        <p>Expire a test-mode authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount</h2>
        <p>Finalize a test-mode authorization's amount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond</h2>
        <p>Respond to fraud challenge</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/increment</h2>
        <p>Increment a test-mode authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/authorizations/{authorization}/reverse</h2>
        <p>Reverse a test-mode authorization</p>


        <h3>Parameters:</h3>
        <ul>

            <li>authorization (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/cards/{card}/shipping/deliver</h2>
        <p>Deliver a testmode card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/cards/{card}/shipping/fail</h2>
        <p>Fail a testmode card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/cards/{card}/shipping/return</h2>
        <p>Return a testmode card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/cards/{card}/shipping/ship</h2>
        <p>Ship a testmode card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/cards/{card}/shipping/submit</h2>
        <p>Submit a testmode card</p>


        <h3>Parameters:</h3>
        <ul>

            <li>card (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate</h2>
        <p>Activate a testmode personalization design</p>


        <h3>Parameters:</h3>
        <ul>

            <li>personalization_design (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate</h2>
        <p>Deactivate a testmode personalization design</p>


        <h3>Parameters:</h3>
        <ul>

            <li>personalization_design (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject</h2>
        <p>Reject a testmode personalization design</p>


        <h3>Parameters:</h3>
        <ul>

            <li>personalization_design (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/settlements</h2>
        <p>Create a test-mode settlement</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/settlements/{settlement}/complete</h2>
        <p>Complete a test-mode settlement</p>


        <h3>Parameters:</h3>
        <ul>

            <li>settlement (path): The settlement token to mark as complete.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/transactions/create_force_capture</h2>
        <p>Create a test-mode force capture</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/transactions/create_unlinked_refund</h2>
        <p>Create a test-mode unlinked refund</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/issuing/transactions/{transaction}/refund</h2>
        <p>Refund a test-mode transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>transaction (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/refunds/{refund}/expire</h2>
        <p>Expire a pending refund.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>refund (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/terminal/readers/{reader}/present_payment_method</h2>
        <p>Simulate presenting a payment method</p>


        <h3>Parameters:</h3>
        <ul>

            <li>reader (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/test_helpers/test_clocks</h2>
        <p>List all test clocks</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/test_clocks</h2>
        <p>Create a test clock</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/test_helpers/test_clocks/{test_clock}</h2>
        <p>Delete a test clock</p>


        <h3>Parameters:</h3>
        <ul>

            <li>test_clock (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/test_helpers/test_clocks/{test_clock}</h2>
        <p>Retrieve a test clock</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>test_clock (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/test_clocks/{test_clock}/advance</h2>
        <p>Advance a test clock</p>


        <h3>Parameters:</h3>
        <ul>

            <li>test_clock (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/inbound_transfers/{id}/fail</h2>
        <p>Test mode: Fail an InboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/inbound_transfers/{id}/return</h2>
        <p>Test mode: Return an InboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/inbound_transfers/{id}/succeed</h2>
        <p>Test mode: Succeed an InboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_payments/{id}</h2>
        <p>Test mode: Update an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_payments/{id}/fail</h2>
        <p>Test mode: Fail an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_payments/{id}/post</h2>
        <p>Test mode: Post an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_payments/{id}/return</h2>
        <p>Test mode: Return an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}</h2>
        <p>Test mode: Update an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail</h2>
        <p>Test mode: Fail an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post</h2>
        <p>Test mode: Post an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return</h2>
        <p>Test mode: Return an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/received_credits</h2>
        <p>Test mode: Create a ReceivedCredit</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/test_helpers/treasury/received_debits</h2>
        <p>Test mode: Create a ReceivedDebit</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/tokens</h2>
        <p>Create a CVC update token</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/tokens/{token}</h2>
        <p>Retrieve a token</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>token (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/topups</h2>
        <p>List all top-ups</p>


        <h3>Parameters:</h3>
        <ul>

            <li>amount (query): A positive integer representing how much to transfer.</li>

            <li>created (query): A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/topups</h2>
        <p>Create a top-up</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/topups/{topup}</h2>
        <p>Retrieve a top-up</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>topup (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/topups/{topup}</h2>
        <p>Update a top-up</p>


        <h3>Parameters:</h3>
        <ul>

            <li>topup (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/topups/{topup}/cancel</h2>
        <p>Cancel a top-up</p>


        <h3>Parameters:</h3>
        <ul>

            <li>topup (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/transfers</h2>
        <p>List all transfers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return transfers that were created during the given date interval.</li>

            <li>destination (query): Only return transfers for the destination specified by this account ID.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>transfer_group (query): Only return transfers with the specified transfer group.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/transfers</h2>
        <p>Create a transfer</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/transfers/{id}/reversals</h2>
        <p>List all reversals</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/transfers/{id}/reversals</h2>
        <p>Create a transfer reversal</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/transfers/{transfer}</h2>
        <p>Retrieve a transfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/transfers/{transfer}</h2>
        <p>Update a transfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/transfers/{transfer}/reversals/{id}</h2>
        <p>Retrieve a reversal</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

            <li>transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/transfers/{transfer}/reversals/{id}</h2>
        <p>Update a reversal</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

            <li>transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/credit_reversals</h2>
        <p>List all CreditReversals</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>received_credit (query): Only return CreditReversals for the ReceivedCredit ID.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return CreditReversals for a given status.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/credit_reversals</h2>
        <p>Create a CreditReversal</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/credit_reversals/{credit_reversal}</h2>
        <p>Retrieve a CreditReversal</p>


        <h3>Parameters:</h3>
        <ul>

            <li>credit_reversal (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/debit_reversals</h2>
        <p>List all DebitReversals</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>received_debit (query): Only return DebitReversals for the ReceivedDebit ID.</li>

            <li>resolution (query): Only return DebitReversals for a given resolution.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return DebitReversals for a given status.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/debit_reversals</h2>
        <p>Create a DebitReversal</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/debit_reversals/{debit_reversal}</h2>
        <p>Retrieve a DebitReversal</p>


        <h3>Parameters:</h3>
        <ul>

            <li>debit_reversal (path): </li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/financial_accounts</h2>
        <p>List all FinancialAccounts</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return FinancialAccounts that were created during the given date interval.</li>

            <li>ending_before (query): An object ID cursor for use in pagination.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit ranging from 1 to 100 (defaults to 10).</li>

            <li>starting_after (query): An object ID cursor for use in pagination.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/financial_accounts</h2>
        <p>Create a FinancialAccount</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/financial_accounts/{financial_account}</h2>
        <p>Retrieve a FinancialAccount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/financial_accounts/{financial_account}</h2>
        <p>Update a FinancialAccount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>financial_account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/financial_accounts/{financial_account}/close</h2>
        <p>Close a FinancialAccount</p>


        <h3>Parameters:</h3>
        <ul>

            <li>financial_account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/financial_accounts/{financial_account}/features</h2>
        <p>Retrieve FinancialAccount Features</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/financial_accounts/{financial_account}/features</h2>
        <p>Update FinancialAccount Features</p>


        <h3>Parameters:</h3>
        <ul>

            <li>financial_account (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/inbound_transfers</h2>
        <p>List all InboundTransfers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/inbound_transfers</h2>
        <p>Create an InboundTransfer</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/inbound_transfers/{id}</h2>
        <p>Retrieve an InboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/inbound_transfers/{inbound_transfer}/cancel</h2>
        <p>Cancel an InboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>inbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/outbound_payments</h2>
        <p>List all OutboundPayments</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return OutboundPayments that were created during the given date interval.</li>

            <li>customer (query): Only return OutboundPayments sent to this customer.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/outbound_payments</h2>
        <p>Create an OutboundPayment</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/outbound_payments/{id}</h2>
        <p>Retrieve an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/outbound_payments/{id}/cancel</h2>
        <p>Cancel an OutboundPayment</p>


        <h3>Parameters:</h3>
        <ul>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/outbound_transfers</h2>
        <p>List all OutboundTransfers</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/outbound_transfers</h2>
        <p>Create an OutboundTransfer</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/outbound_transfers/{outbound_transfer}</h2>
        <p>Retrieve an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/treasury/outbound_transfers/{outbound_transfer}/cancel</h2>
        <p>Cancel an OutboundTransfer</p>


        <h3>Parameters:</h3>
        <ul>

            <li>outbound_transfer (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/received_credits</h2>
        <p>List all ReceivedCredits</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): The FinancialAccount that received the funds.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>linked_flows (query): Only return ReceivedCredits described by the flow.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return ReceivedCredits that have the given status: `succeeded` or `failed`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/received_credits/{id}</h2>
        <p>Retrieve a ReceivedCredit</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/received_debits</h2>
        <p>List all ReceivedDebits</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): The FinancialAccount that funds were pulled from.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return ReceivedDebits that have the given status: `succeeded` or `failed`.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/received_debits/{id}</h2>
        <p>Retrieve a ReceivedDebit</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/transaction_entries</h2>
        <p>List all TransactionEntries</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return TransactionEntries that were created during the given date interval.</li>

            <li>effective_at (query): </li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>order_by (query): The results are in reverse chronological order by `created` or `effective_at`. The default is `created`.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>transaction (query): Only return TransactionEntries associated with this Transaction.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/transaction_entries/{id}</h2>
        <p>Retrieve a TransactionEntry</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/transactions</h2>
        <p>List all Transactions</p>


        <h3>Parameters:</h3>
        <ul>

            <li>created (query): Only return Transactions that were created during the given date interval.</li>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>financial_account (query): Returns objects associated with this FinancialAccount.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>order_by (query): The results are in reverse chronological order by `created` or `posted_at`. The default is `created`.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

            <li>status (query): Only return Transactions that have the given status: `open`, `posted`, or `void`.</li>

            <li>status_transitions (query): A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/treasury/transactions/{id}</h2>
        <p>Retrieve a Transaction</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>id (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/webhook_endpoints</h2>
        <p>List all webhook endpoints</p>


        <h3>Parameters:</h3>
        <ul>

            <li>ending_before (query): A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.</li>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>limit (query): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.</li>

            <li>starting_after (query): A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/webhook_endpoints</h2>
        <p>Create a webhook endpoint</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /v1/webhook_endpoints/{webhook_endpoint}</h2>
        <p>Delete a webhook endpoint</p>


        <h3>Parameters:</h3>
        <ul>

            <li>webhook_endpoint (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>GET - /v1/webhook_endpoints/{webhook_endpoint}</h2>
        <p>Retrieve a webhook endpoint</p>


        <h3>Parameters:</h3>
        <ul>

            <li>expand (query): Specifies which fields in the response should be expanded.</li>

            <li>webhook_endpoint (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

    <div>
        <h2>POST - /v1/webhook_endpoints/{webhook_endpoint}</h2>
        <p>Update a webhook endpoint</p>


        <h3>Parameters:</h3>
        <ul>

            <li>webhook_endpoint (path): </li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Successful response.</li>

            <li>default: Error response.</li>

        </ul>
    </div>

</body>
</html>
