# gitee.UsersApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_user_following_username**](UsersApi.md#delete_v5_user_following_username) | **DELETE** /v5/user/following/{username} | 取消关注一个用户
[**delete_v5_user_keys_id**](UsersApi.md#delete_v5_user_keys_id) | **DELETE** /v5/user/keys/{id} | 删除一个公钥
[**get_v5_user**](UsersApi.md#get_v5_user) | **GET** /v5/user | 获取授权用户的资料
[**get_v5_user_followers**](UsersApi.md#get_v5_user_followers) | **GET** /v5/user/followers | 列出授权用户的关注者
[**get_v5_user_following**](UsersApi.md#get_v5_user_following) | **GET** /v5/user/following | 列出授权用户正关注的用户
[**get_v5_user_following_username**](UsersApi.md#get_v5_user_following_username) | **GET** /v5/user/following/{username} | 检查授权用户是否关注了一个用户
[**get_v5_user_keys**](UsersApi.md#get_v5_user_keys) | **GET** /v5/user/keys | 列出授权用户的所有公钥
[**get_v5_user_keys_id**](UsersApi.md#get_v5_user_keys_id) | **GET** /v5/user/keys/{id} | 获取一个公钥
[**get_v5_user_namespace**](UsersApi.md#get_v5_user_namespace) | **GET** /v5/user/namespace | 获取授权用户的一个 Namespace
[**get_v5_user_namespaces**](UsersApi.md#get_v5_user_namespaces) | **GET** /v5/user/namespaces | 列出授权用户所有的 Namespace
[**get_v5_users_username**](UsersApi.md#get_v5_users_username) | **GET** /v5/users/{username} | 获取一个用户
[**get_v5_users_username_followers**](UsersApi.md#get_v5_users_username_followers) | **GET** /v5/users/{username}/followers | 列出指定用户的关注者
[**get_v5_users_username_following**](UsersApi.md#get_v5_users_username_following) | **GET** /v5/users/{username}/following | 列出指定用户正在关注的用户
[**get_v5_users_username_following_target_user**](UsersApi.md#get_v5_users_username_following_target_user) | **GET** /v5/users/{username}/following/{target_user} | 检查指定用户是否关注目标用户
[**get_v5_users_username_keys**](UsersApi.md#get_v5_users_username_keys) | **GET** /v5/users/{username}/keys | 列出指定用户的所有公钥
[**patch_v5_user**](UsersApi.md#patch_v5_user) | **PATCH** /v5/user | 更新授权用户的资料
[**post_v5_user_keys**](UsersApi.md#post_v5_user_keys) | **POST** /v5/user/keys | 添加一个公钥
[**put_v5_user_following_username**](UsersApi.md#put_v5_user_following_username) | **PUT** /v5/user/following/{username} | 关注一个用户

# **delete_v5_user_following_username**
> delete_v5_user_following_username(username, access_token=access_token)

取消关注一个用户

取消关注一个用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消关注一个用户
    api_instance.delete_v5_user_following_username(username, access_token=access_token)
except ApiException as e:
    print("Exception when calling UsersApi->delete_v5_user_following_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_user_keys_id**
> delete_v5_user_keys_id(id, access_token=access_token)

删除一个公钥

删除一个公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个公钥
    api_instance.delete_v5_user_keys_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling UsersApi->delete_v5_user_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user**
> UserDetail get_v5_user(access_token=access_token)

获取授权用户的资料

获取授权用户的资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的资料
    api_response = api_instance.get_v5_user(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_followers**
> list[UserBasic] get_v5_user_followers(access_token=access_token, page=page, per_page=per_page)

列出授权用户的关注者

列出授权用户的关注者

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的关注者
    api_response = api_instance.get_v5_user_followers(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserBasic]**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_following**
> list[UserBasic] get_v5_user_following(access_token=access_token, page=page, per_page=per_page)

列出授权用户正关注的用户

列出授权用户正关注的用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户正关注的用户
    api_response = api_instance.get_v5_user_following(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserBasic]**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_following_username**
> get_v5_user_following_username(username, access_token=access_token)

检查授权用户是否关注了一个用户

检查授权用户是否关注了一个用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否关注了一个用户
    api_instance.get_v5_user_following_username(username, access_token=access_token)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_following_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_keys**
> list[SSHKey] get_v5_user_keys(access_token=access_token, page=page, per_page=per_page)

列出授权用户的所有公钥

列出授权用户的所有公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有公钥
    api_response = api_instance.get_v5_user_keys(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[SSHKey]**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_keys_id**
> SSHKey get_v5_user_keys_id(id, access_token=access_token)

获取一个公钥

获取一个公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个公钥
    api_response = api_instance.get_v5_user_keys_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_namespace**
> list[Namespace] get_v5_user_namespace(path, access_token=access_token)

获取授权用户的一个 Namespace

获取授权用户的一个 Namespace

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
path = 'path_example' # str | Namespace path
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的一个 Namespace
    api_response = api_instance.get_v5_user_namespace(path, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Namespace path | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[Namespace]**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_namespaces**
> list[Namespace] get_v5_user_namespaces(access_token=access_token, mode=mode)

列出授权用户所有的 Namespace

列出授权用户所有的 Namespace

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
mode = 'mode_example' # str | 参与方式: project(所有参与仓库的namepsce)、intrant(所加入的namespace)、all(包含前两者)，默认(intrant) (optional)

try:
    # 列出授权用户所有的 Namespace
    api_response = api_instance.get_v5_user_namespaces(access_token=access_token, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_user_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **mode** | **str**| 参与方式: project(所有参与仓库的namepsce)、intrant(所加入的namespace)、all(包含前两者)，默认(intrant) | [optional] 

### Return type

[**list[Namespace]**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username**
> UserInfo get_v5_users_username(username, access_token=access_token)

获取一个用户

获取一个用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个用户
    api_response = api_instance.get_v5_users_username(username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_users_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_followers**
> list[UserBasic] get_v5_users_username_followers(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户的关注者

列出指定用户的关注者

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出指定用户的关注者
    api_response = api_instance.get_v5_users_username_followers(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_users_username_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserBasic]**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_following**
> list[UserBasic] get_v5_users_username_following(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户正在关注的用户

列出指定用户正在关注的用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出指定用户正在关注的用户
    api_response = api_instance.get_v5_users_username_following(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_users_username_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserBasic]**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_following_target_user**
> get_v5_users_username_following_target_user(username, target_user, access_token=access_token)

检查指定用户是否关注目标用户

检查指定用户是否关注目标用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
target_user = 'target_user_example' # str | 目标用户的用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查指定用户是否关注目标用户
    api_instance.get_v5_users_username_following_target_user(username, target_user, access_token=access_token)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_users_username_following_target_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **target_user** | **str**| 目标用户的用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_keys**
> list[SSHKeyBasic] get_v5_users_username_keys(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户的所有公钥

列出指定用户的所有公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出指定用户的所有公钥
    api_response = api_instance.get_v5_users_username_keys(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_v5_users_username_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[SSHKeyBasic]**](SSHKeyBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_user**
> User patch_v5_user(access_token=access_token, name=name, blog=blog, weibo=weibo, bio=bio)

更新授权用户的资料

更新授权用户的资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
access_token = 'access_token_example' # str |  (optional)
name = 'name_example' # str |  (optional)
blog = 'blog_example' # str |  (optional)
weibo = 'weibo_example' # str |  (optional)
bio = 'bio_example' # str |  (optional)

try:
    # 更新授权用户的资料
    api_response = api_instance.patch_v5_user(access_token=access_token, name=name, blog=blog, weibo=weibo, bio=bio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_v5_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **blog** | **str**|  | [optional] 
 **weibo** | **str**|  | [optional] 
 **bio** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_user_keys**
> SSHKey post_v5_user_keys(body)

添加一个公钥

添加一个公钥

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
body = gitee.Body44() # Body44 | 

try:
    # 添加一个公钥
    api_response = api_instance.post_v5_user_keys(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_v5_user_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body44**](Body44.md)|  | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_user_following_username**
> put_v5_user_following_username(username, body=body)

关注一个用户

关注一个用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.UsersApi()
username = 'username_example' # str | 用户名(username/login)
body = gitee.Body48() # Body48 |  (optional)

try:
    # 关注一个用户
    api_instance.put_v5_user_following_username(username, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->put_v5_user_following_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **body** | [**Body48**](Body48.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

