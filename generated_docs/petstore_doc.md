<p><!DOCTYPE html></p>

<html>
<head>
    <title>Swagger Petstore - OpenAPI 3.0 Documentation</title>
</head>
<body>
    <h1>Swagger Petstore - OpenAPI 3.0 (Version 1.0.27-SNAPSHOT)</h1>

    <div>
        <h2>PUT - /pet</h2>
        <p>Update an existing pet.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful operation</li>

            <li>400: Invalid ID supplied</li>

            <li>404: Pet not found</li>

            <li>422: Validation exception</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /pet</h2>
        <p>Add a new pet to the store.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful operation</li>

            <li>400: Invalid input</li>

            <li>422: Validation exception</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /pet/findByStatus</h2>
        <p>Finds Pets by status.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>status (query): Status values that need to be considered for filter</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid status value</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /pet/findByTags</h2>
        <p>Finds Pets by tags.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>tags (query): Tags to filter by</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid tag value</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /pet/{petId}</h2>
        <p>Find pet by ID.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>petId (path): ID of pet to return</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid ID supplied</li>

            <li>404: Pet not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /pet/{petId}</h2>
        <p>Updates a pet in the store with form data.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>petId (path): ID of pet that needs to be updated</li>

            <li>name (query): Name of pet that needs to be updated</li>

            <li>status (query): Status of pet that needs to be updated</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid input</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /pet/{petId}</h2>
        <p>Deletes a pet.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>api_key (header): </li>

            <li>petId (path): Pet id to delete</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: Pet deleted</li>

            <li>400: Invalid pet value</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /pet/{petId}/uploadImage</h2>
        <p>Uploads an image.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>petId (path): ID of pet to update</li>

            <li>additionalMetadata (query): Additional Metadata</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: No file uploaded</li>

            <li>404: Pet not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /store/inventory</h2>
        <p>Returns pet inventories by status.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /store/order</h2>
        <p>Place an order for a pet.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid input</li>

            <li>422: Validation exception</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /store/order/{orderId}</h2>
        <p>Find purchase order by ID.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>orderId (path): ID of order that needs to be fetched</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid ID supplied</li>

            <li>404: Order not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /store/order/{orderId}</h2>
        <p>Delete purchase order by identifier.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>orderId (path): ID of the order that needs to be deleted</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: order deleted</li>

            <li>400: Invalid ID supplied</li>

            <li>404: Order not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /user</h2>
        <p>Create user.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>POST - /user/createWithList</h2>
        <p>Creates list of users with given input array.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: Successful operation</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /user/login</h2>
        <p>Logs user into the system.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>username (query): The user name for login</li>

            <li>password (query): The password for login in clear text</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid username/password supplied</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /user/logout</h2>
        <p>Logs out current logged in user session.</p>



        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>GET - /user/{username}</h2>
        <p>Get user by user name.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>username (path): The name that needs to be fetched. Use user1 for testing</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: Invalid username supplied</li>

            <li>404: User not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>PUT - /user/{username}</h2>
        <p>Update user resource.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>username (path): name that need to be deleted</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: successful operation</li>

            <li>400: bad request</li>

            <li>404: user not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

    <div>
        <h2>DELETE - /user/{username}</h2>
        <p>Delete user resource.</p>


        <h3>Parameters:</h3>
        <ul>

            <li>username (path): The name that needs to be deleted</li>

        </ul>


        <h3>Responses:</h3>
        <ul>

            <li>200: User deleted</li>

            <li>400: Invalid username supplied</li>

            <li>404: User not found</li>

            <li>default: Unexpected error</li>

        </ul>
    </div>

</body>
</html>
