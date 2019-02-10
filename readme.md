**Fashion Cloud Catalog API**

This challenge runs on flask.

* Please perform a `pip install -r requirements.txt` and make a `POST` request to `http://127.0.0.1:5000/`
* The only endpoint is a `POST` based one.

* Flask runs the server on `http://127.0.0.1:5000/` by default.

* The API supports extra payload like the following:

    ```json
    {  
      "custom_fields":[  
        {  
          "tag":"price_buy_net_currency",
          "fields":[  
            "price_buy_net",
            "currency"
          ]
        }
      ],
      "grouping_keys":[  
        "article_structure",
        "color",
        "brand"
      ]
    }
    ```   
* The `grouping_keys` field tells the API to group the catalog with the given keys. 
The first key is the parent followed by further groupings. Please note that only 3 keys
 are supported.
 
* The `custom_fields` field tells the API to combine two or more fields into a single 
field with the `tag` as defined in the custom field object. The API supports multiple 
`custom_fields` objects.

* The testing of the API is implemented using `pytest` and tests both of the features 
defined above. To run the test, simple run `pytest`



