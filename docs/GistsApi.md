# gitee.GistsApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_gists_gist_id_comments_id**](GistsApi.md#delete_v5_gists_gist_id_comments_id) | **DELETE** /v5/gists/{gist_id}/comments/{id} | 删除代码片段的评论
[**delete_v5_gists_id**](GistsApi.md#delete_v5_gists_id) | **DELETE** /v5/gists/{id} | 删除指定代码片段
[**delete_v5_gists_id_star**](GistsApi.md#delete_v5_gists_id_star) | **DELETE** /v5/gists/{id}/star | 取消Star代码片段
[**get_v5_gists**](GistsApi.md#get_v5_gists) | **GET** /v5/gists | 获取代码片段
[**get_v5_gists_gist_id_comments**](GistsApi.md#get_v5_gists_gist_id_comments) | **GET** /v5/gists/{gist_id}/comments | 获取代码片段的评论
[**get_v5_gists_gist_id_comments_id**](GistsApi.md#get_v5_gists_gist_id_comments_id) | **GET** /v5/gists/{gist_id}/comments/{id} | 获取单条代码片段的评论
[**get_v5_gists_id**](GistsApi.md#get_v5_gists_id) | **GET** /v5/gists/{id} | 获取单条代码片段
[**get_v5_gists_id_commits**](GistsApi.md#get_v5_gists_id_commits) | **GET** /v5/gists/{id}/commits | 获取代码片段的commit
[**get_v5_gists_id_forks**](GistsApi.md#get_v5_gists_id_forks) | **GET** /v5/gists/{id}/forks | 获取 Fork 了指定代码片段的列表
[**get_v5_gists_id_star**](GistsApi.md#get_v5_gists_id_star) | **GET** /v5/gists/{id}/star | 判断代码片段是否已Star
[**get_v5_gists_starred**](GistsApi.md#get_v5_gists_starred) | **GET** /v5/gists/starred | 获取用户Star的代码片段
[**patch_v5_gists_gist_id_comments_id**](GistsApi.md#patch_v5_gists_gist_id_comments_id) | **PATCH** /v5/gists/{gist_id}/comments/{id} | 修改代码片段的评论
[**patch_v5_gists_id**](GistsApi.md#patch_v5_gists_id) | **PATCH** /v5/gists/{id} | 修改代码片段
[**post_v5_gists**](GistsApi.md#post_v5_gists) | **POST** /v5/gists | 创建代码片段
[**post_v5_gists_gist_id_comments**](GistsApi.md#post_v5_gists_gist_id_comments) | **POST** /v5/gists/{gist_id}/comments | 增加代码片段的评论
[**post_v5_gists_id_forks**](GistsApi.md#post_v5_gists_id_forks) | **POST** /v5/gists/{id}/forks | Fork代码片段
[**put_v5_gists_id_star**](GistsApi.md#put_v5_gists_id_star) | **PUT** /v5/gists/{id}/star | Star代码片段

# **delete_v5_gists_gist_id_comments_id**
> delete_v5_gists_gist_id_comments_id(gist_id, id, access_token=access_token)

删除代码片段的评论

删除代码片段的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除代码片段的评论
    api_instance.delete_v5_gists_gist_id_comments_id(gist_id, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->delete_v5_gists_gist_id_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_gists_id**
> delete_v5_gists_id(id, access_token=access_token)

删除指定代码片段

删除指定代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除指定代码片段
    api_instance.delete_v5_gists_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->delete_v5_gists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_gists_id_star**
> delete_v5_gists_id_star(id, access_token=access_token)

取消Star代码片段

取消Star代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消Star代码片段
    api_instance.delete_v5_gists_id_star(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->delete_v5_gists_id_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists**
> list[Code] get_v5_gists(access_token=access_token, since=since, page=page, per_page=per_page)

获取代码片段

获取代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取代码片段
    api_response = api_instance.get_v5_gists(access_token=access_token, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Code]**](Code.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_gist_id_comments**
> list[CodeComment] get_v5_gists_gist_id_comments(gist_id, access_token=access_token, page=page, per_page=per_page)

获取代码片段的评论

获取代码片段的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
gist_id = 'gist_id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取代码片段的评论
    api_response = api_instance.get_v5_gists_gist_id_comments(gist_id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_gist_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[CodeComment]**](CodeComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_gist_id_comments_id**
> CodeComment get_v5_gists_gist_id_comments_id(gist_id, id, access_token=access_token)

获取单条代码片段的评论

获取单条代码片段的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单条代码片段的评论
    api_response = api_instance.get_v5_gists_gist_id_comments_id(gist_id, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_gist_id_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**CodeComment**](CodeComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_id**
> CodeForksHistory get_v5_gists_id(id, access_token=access_token)

获取单条代码片段

获取单条代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单条代码片段
    api_response = api_instance.get_v5_gists_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**CodeForksHistory**](CodeForksHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_id_commits**
> CodeForksHistory get_v5_gists_id_commits(id, access_token=access_token)

获取代码片段的commit

获取代码片段的commit

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取代码片段的commit
    api_response = api_instance.get_v5_gists_id_commits(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_id_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**CodeForksHistory**](CodeForksHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_id_forks**
> CodeForks get_v5_gists_id_forks(id, access_token=access_token, page=page, per_page=per_page)

获取 Fork 了指定代码片段的列表

获取 Fork 了指定代码片段的列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取 Fork 了指定代码片段的列表
    api_response = api_instance.get_v5_gists_id_forks(id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_id_forks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**CodeForks**](CodeForks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_id_star**
> get_v5_gists_id_star(id, access_token=access_token)

判断代码片段是否已Star

判断代码片段是否已Star

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断代码片段是否已Star
    api_instance.get_v5_gists_id_star(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_id_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gists_starred**
> list[Code] get_v5_gists_starred(access_token=access_token, since=since, page=page, per_page=per_page)

获取用户Star的代码片段

获取用户Star的代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取用户Star的代码片段
    api_response = api_instance.get_v5_gists_starred(access_token=access_token, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->get_v5_gists_starred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Code]**](Code.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_gists_gist_id_comments_id**
> CodeComment patch_v5_gists_gist_id_comments_id(access_token, body, gist_id, id)

修改代码片段的评论

修改代码片段的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
access_token = 'access_token_example' # str | 
body = 'body_example' # str | 
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID

try:
    # 修改代码片段的评论
    api_response = api_instance.patch_v5_gists_gist_id_comments_id(access_token, body, gist_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->patch_v5_gists_gist_id_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **body** | **str**|  | 
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 

### Return type

[**CodeComment**](CodeComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_gists_id**
> CodeForksHistory patch_v5_gists_id(id, access_token=access_token, files=files, description=description, public=public)

修改代码片段

修改代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str |  (optional)
files = NULL # object |  (optional)
description = 'description_example' # str |  (optional)
public = true # bool |  (optional)

try:
    # 修改代码片段
    api_response = api_instance.patch_v5_gists_id(id, access_token=access_token, files=files, description=description, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->patch_v5_gists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**|  | [optional] 
 **files** | [**object**](.md)|  | [optional] 
 **description** | **str**|  | [optional] 
 **public** | **bool**|  | [optional] 

### Return type

[**CodeForksHistory**](CodeForksHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_gists**
> list[CodeForksHistory] post_v5_gists(body)

创建代码片段

创建代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
body = gitee.Body51() # Body51 | 

try:
    # 创建代码片段
    api_response = api_instance.post_v5_gists(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->post_v5_gists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body51**](Body51.md)|  | 

### Return type

[**list[CodeForksHistory]**](CodeForksHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_gists_gist_id_comments**
> CodeComment post_v5_gists_gist_id_comments(body, gist_id)

增加代码片段的评论

增加代码片段的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
body = gitee.Body52() # Body52 | 
gist_id = 'gist_id_example' # str | 代码片段的ID

try:
    # 增加代码片段的评论
    api_response = api_instance.post_v5_gists_gist_id_comments(body, gist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->post_v5_gists_gist_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body52**](Body52.md)|  | 
 **gist_id** | **str**| 代码片段的ID | 

### Return type

[**CodeComment**](CodeComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_gists_id_forks**
> post_v5_gists_id_forks(id, body=body)

Fork代码片段

Fork代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
body = gitee.Body56() # Body56 |  (optional)

try:
    # Fork代码片段
    api_instance.post_v5_gists_id_forks(id, body=body)
except ApiException as e:
    print("Exception when calling GistsApi->post_v5_gists_id_forks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **body** | [**Body56**](Body56.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_gists_id_star**
> put_v5_gists_id_star(id, body=body)

Star代码片段

Star代码片段

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GistsApi()
id = 'id_example' # str | 代码片段的ID
body = gitee.Body55() # Body55 |  (optional)

try:
    # Star代码片段
    api_instance.put_v5_gists_id_star(id, body=body)
except ApiException as e:
    print("Exception when calling GistsApi->put_v5_gists_id_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **body** | [**Body55**](Body55.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

