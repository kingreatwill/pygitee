# gitee

pygitee 是封装了gitee的OpenAPI的python库.

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

```python
pip install pygitee
```

Then import the package:
```python
import gitee 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gitee
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 star 一个仓库
    api_instance.delete_v5_user_starred_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_v5_user_starred_owner_repo: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 watch 一个仓库
    api_instance.delete_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_v5_user_subscriptions_owner_repo: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的所有公开动态
    api_response = api_instance.get_v5_networks_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_networks_owner_repo_events: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)

try:
    # 获取授权用户的通知数
    api_response = api_instance.get_v5_notifications_count(access_token=access_token, unread=unread)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_count: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只显示未读私信，默认：否 (optional)
since = 'since_example' # str | 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组私信 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有私信
    api_response = api_instance.get_v5_notifications_messages(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_messages: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
id = 'id_example' # str | 私信的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条私信
    api_response = api_instance.get_v5_notifications_messages_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_messages_id: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'all' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional) (default to all)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有通知
    api_response = api_instance.get_v5_notifications_threads(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_threads: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
id = 'id_example' # str | 通知的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条通知
    api_response = api_instance.get_v5_notifications_threads_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_threads_id: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出组织的公开动态
    api_response = api_instance.get_v5_orgs_org_events(org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_orgs_org_events: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的所有动态
    api_response = api_instance.get_v5_repos_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_events: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'all' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional) (default to all)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个仓库里的通知
    api_response = api_instance.get_v5_repos_owner_repo_notifications(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_notifications: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出 star 了仓库的用户
    api_response = api_instance.get_v5_repos_owner_repo_stargazers(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_stargazers: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出 watch 了仓库的用户
    api_response = api_instance.get_v5_repos_owner_repo_subscribers(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_subscribers: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户 star 了的仓库
    api_response = api_instance.get_v5_user_starred(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_starred: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 star 了一个仓库
    api_instance.get_v5_user_starred_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_starred_owner_repo: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户 watch 了的仓库
    api_response = api_instance.get_v5_user_subscriptions(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_subscriptions: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 watch 了一个仓库
    api_instance.get_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_subscriptions_owner_repo: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户的动态
    api_response = api_instance.get_v5_users_username_events(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户所属组织的动态
    api_response = api_instance.get_v5_users_username_events_orgs_org(username, org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events_orgs_org: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户的公开动态
    api_response = api_instance.get_v5_users_username_events_public(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events_public: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个用户收到的动态
    api_response = api_instance.get_v5_users_username_received_events(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_received_events: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个用户收到的公开动态
    api_response = api_instance.get_v5_users_username_received_events_public(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_received_events_public: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 列出用户 star 了的仓库
    api_response = api_instance.get_v5_users_username_starred(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_starred: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 列出用户 watch 了的仓库
    api_response = api_instance.get_v5_users_username_subscriptions(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_subscriptions: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
id = 'id_example' # str | 私信的 ID
access_token = 'access_token_example' # str |  (optional)

try:
    # 标记一条私信为已读
    api_instance.patch_v5_notifications_messages_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->patch_v5_notifications_messages_id: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
id = 'id_example' # str | 通知的 ID
access_token = 'access_token_example' # str |  (optional)

try:
    # 标记一条通知为已读
    api_instance.patch_v5_notifications_threads_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->patch_v5_notifications_threads_id: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
body = gitee.Body71() # Body71 | 

try:
    # 发送私信给指定用户
    api_response = api_instance.post_v5_notifications_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->post_v5_notifications_messages: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
body = gitee.Body70() # Body70 |  (optional)

try:
    # 标记所有私信为已读
    api_instance.put_v5_notifications_messages(body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_notifications_messages: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
body = gitee.Body68() # Body68 |  (optional)

try:
    # 标记所有通知为已读
    api_instance.put_v5_notifications_threads(body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_notifications_threads: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.Body43() # Body43 |  (optional)

try:
    # 标记一个仓库里的通知为已读
    api_instance.put_v5_repos_owner_repo_notifications(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_repos_owner_repo_notifications: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.Body49() # Body49 |  (optional)

try:
    # star 一个仓库
    api_instance.put_v5_user_starred_owner_repo(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_user_starred_owner_repo: %s\n" % e)

# create an instance of the API class
api_instance = gitee.ActivityApi(gitee.ApiClient(configuration))
body = gitee.Body50() # Body50 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # watch 一个仓库
    api_instance.put_v5_user_subscriptions_owner_repo(body, owner, repo)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_user_subscriptions_owner_repo: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//https://gitee.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivityApi* | [**delete_v5_user_starred_owner_repo**](docs/ActivityApi.md#delete_v5_user_starred_owner_repo) | **DELETE** /v5/user/starred/{owner}/{repo} | 取消 star 一个仓库
*ActivityApi* | [**delete_v5_user_subscriptions_owner_repo**](docs/ActivityApi.md#delete_v5_user_subscriptions_owner_repo) | **DELETE** /v5/user/subscriptions/{owner}/{repo} | 取消 watch 一个仓库
*ActivityApi* | [**get_v5_networks_owner_repo_events**](docs/ActivityApi.md#get_v5_networks_owner_repo_events) | **GET** /v5/networks/{owner}/{repo}/events | 列出仓库的所有公开动态
*ActivityApi* | [**get_v5_notifications_count**](docs/ActivityApi.md#get_v5_notifications_count) | **GET** /v5/notifications/count | 获取授权用户的通知数
*ActivityApi* | [**get_v5_notifications_messages**](docs/ActivityApi.md#get_v5_notifications_messages) | **GET** /v5/notifications/messages | 列出授权用户的所有私信
*ActivityApi* | [**get_v5_notifications_messages_id**](docs/ActivityApi.md#get_v5_notifications_messages_id) | **GET** /v5/notifications/messages/{id} | 获取一条私信
*ActivityApi* | [**get_v5_notifications_threads**](docs/ActivityApi.md#get_v5_notifications_threads) | **GET** /v5/notifications/threads | 列出授权用户的所有通知
*ActivityApi* | [**get_v5_notifications_threads_id**](docs/ActivityApi.md#get_v5_notifications_threads_id) | **GET** /v5/notifications/threads/{id} | 获取一条通知
*ActivityApi* | [**get_v5_orgs_org_events**](docs/ActivityApi.md#get_v5_orgs_org_events) | **GET** /v5/orgs/{org}/events | 列出组织的公开动态
*ActivityApi* | [**get_v5_repos_owner_repo_events**](docs/ActivityApi.md#get_v5_repos_owner_repo_events) | **GET** /v5/repos/{owner}/{repo}/events | 列出仓库的所有动态
*ActivityApi* | [**get_v5_repos_owner_repo_notifications**](docs/ActivityApi.md#get_v5_repos_owner_repo_notifications) | **GET** /v5/repos/{owner}/{repo}/notifications | 列出一个仓库里的通知
*ActivityApi* | [**get_v5_repos_owner_repo_stargazers**](docs/ActivityApi.md#get_v5_repos_owner_repo_stargazers) | **GET** /v5/repos/{owner}/{repo}/stargazers | 列出 star 了仓库的用户
*ActivityApi* | [**get_v5_repos_owner_repo_subscribers**](docs/ActivityApi.md#get_v5_repos_owner_repo_subscribers) | **GET** /v5/repos/{owner}/{repo}/subscribers | 列出 watch 了仓库的用户
*ActivityApi* | [**get_v5_user_starred**](docs/ActivityApi.md#get_v5_user_starred) | **GET** /v5/user/starred | 列出授权用户 star 了的仓库
*ActivityApi* | [**get_v5_user_starred_owner_repo**](docs/ActivityApi.md#get_v5_user_starred_owner_repo) | **GET** /v5/user/starred/{owner}/{repo} | 检查授权用户是否 star 了一个仓库
*ActivityApi* | [**get_v5_user_subscriptions**](docs/ActivityApi.md#get_v5_user_subscriptions) | **GET** /v5/user/subscriptions | 列出授权用户 watch 了的仓库
*ActivityApi* | [**get_v5_user_subscriptions_owner_repo**](docs/ActivityApi.md#get_v5_user_subscriptions_owner_repo) | **GET** /v5/user/subscriptions/{owner}/{repo} | 检查授权用户是否 watch 了一个仓库
*ActivityApi* | [**get_v5_users_username_events**](docs/ActivityApi.md#get_v5_users_username_events) | **GET** /v5/users/{username}/events | 列出用户的动态
*ActivityApi* | [**get_v5_users_username_events_orgs_org**](docs/ActivityApi.md#get_v5_users_username_events_orgs_org) | **GET** /v5/users/{username}/events/orgs/{org} | 列出用户所属组织的动态
*ActivityApi* | [**get_v5_users_username_events_public**](docs/ActivityApi.md#get_v5_users_username_events_public) | **GET** /v5/users/{username}/events/public | 列出用户的公开动态
*ActivityApi* | [**get_v5_users_username_received_events**](docs/ActivityApi.md#get_v5_users_username_received_events) | **GET** /v5/users/{username}/received_events | 列出一个用户收到的动态
*ActivityApi* | [**get_v5_users_username_received_events_public**](docs/ActivityApi.md#get_v5_users_username_received_events_public) | **GET** /v5/users/{username}/received_events/public | 列出一个用户收到的公开动态
*ActivityApi* | [**get_v5_users_username_starred**](docs/ActivityApi.md#get_v5_users_username_starred) | **GET** /v5/users/{username}/starred | 列出用户 star 了的仓库
*ActivityApi* | [**get_v5_users_username_subscriptions**](docs/ActivityApi.md#get_v5_users_username_subscriptions) | **GET** /v5/users/{username}/subscriptions | 列出用户 watch 了的仓库
*ActivityApi* | [**patch_v5_notifications_messages_id**](docs/ActivityApi.md#patch_v5_notifications_messages_id) | **PATCH** /v5/notifications/messages/{id} | 标记一条私信为已读
*ActivityApi* | [**patch_v5_notifications_threads_id**](docs/ActivityApi.md#patch_v5_notifications_threads_id) | **PATCH** /v5/notifications/threads/{id} | 标记一条通知为已读
*ActivityApi* | [**post_v5_notifications_messages**](docs/ActivityApi.md#post_v5_notifications_messages) | **POST** /v5/notifications/messages | 发送私信给指定用户
*ActivityApi* | [**put_v5_notifications_messages**](docs/ActivityApi.md#put_v5_notifications_messages) | **PUT** /v5/notifications/messages | 标记所有私信为已读
*ActivityApi* | [**put_v5_notifications_threads**](docs/ActivityApi.md#put_v5_notifications_threads) | **PUT** /v5/notifications/threads | 标记所有通知为已读
*ActivityApi* | [**put_v5_repos_owner_repo_notifications**](docs/ActivityApi.md#put_v5_repos_owner_repo_notifications) | **PUT** /v5/repos/{owner}/{repo}/notifications | 标记一个仓库里的通知为已读
*ActivityApi* | [**put_v5_user_starred_owner_repo**](docs/ActivityApi.md#put_v5_user_starred_owner_repo) | **PUT** /v5/user/starred/{owner}/{repo} | star 一个仓库
*ActivityApi* | [**put_v5_user_subscriptions_owner_repo**](docs/ActivityApi.md#put_v5_user_subscriptions_owner_repo) | **PUT** /v5/user/subscriptions/{owner}/{repo} | watch 一个仓库
*EmailsApi* | [**get_v5_emails**](docs/EmailsApi.md#get_v5_emails) | **GET** /v5/emails | 获取授权用户的全部邮箱
*EnterprisesApi* | [**delete_v5_enterprises_enterprise_members_username**](docs/EnterprisesApi.md#delete_v5_enterprises_enterprise_members_username) | **DELETE** /v5/enterprises/{enterprise}/members/{username} | 移除企业成员
*EnterprisesApi* | [**delete_v5_enterprises_enterprise_week_reports_report_id_comments_id**](docs/EnterprisesApi.md#delete_v5_enterprises_enterprise_week_reports_report_id_comments_id) | **DELETE** /v5/enterprises/{enterprise}/week_reports/{report_id}/comments/{id} | 删除周报某个评论
*EnterprisesApi* | [**get_v5_enterprise_enterprise_pull_requests**](docs/EnterprisesApi.md#get_v5_enterprise_enterprise_pull_requests) | **GET** /v5/enterprise/{enterprise}/pull_requests | 企业Pull Reuqest 列表
*EnterprisesApi* | [**get_v5_enterprises_enterprise**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise) | **GET** /v5/enterprises/{enterprise} | 获取一个企业
*EnterprisesApi* | [**get_v5_enterprises_enterprise_members**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_members) | **GET** /v5/enterprises/{enterprise}/members | 列出企业的所有成员
*EnterprisesApi* | [**get_v5_enterprises_enterprise_members_username**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_members_username) | **GET** /v5/enterprises/{enterprise}/members/{username} | 获取企业的一个成员
*EnterprisesApi* | [**get_v5_enterprises_enterprise_users_username_week_reports**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_users_username_week_reports) | **GET** /v5/enterprises/{enterprise}/users/{username}/week_reports | 个人周报列表
*EnterprisesApi* | [**get_v5_enterprises_enterprise_week_reports**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports) | **GET** /v5/enterprises/{enterprise}/week_reports | 企业成员周报列表
*EnterprisesApi* | [**get_v5_enterprises_enterprise_week_reports_id**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports_id) | **GET** /v5/enterprises/{enterprise}/week_reports/{id} | 周报详情
*EnterprisesApi* | [**get_v5_enterprises_enterprise_week_reports_id_comments**](docs/EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports_id_comments) | **GET** /v5/enterprises/{enterprise}/week_reports/{id}/comments | 某个周报评论列表
*EnterprisesApi* | [**get_v5_user_enterprises**](docs/EnterprisesApi.md#get_v5_user_enterprises) | **GET** /v5/user/enterprises | 列出授权用户所属的企业
*EnterprisesApi* | [**patch_v5_enterprises_enterprise_week_report_id**](docs/EnterprisesApi.md#patch_v5_enterprises_enterprise_week_report_id) | **PATCH** /v5/enterprises/{enterprise}/week_report/{id} | 编辑周报
*EnterprisesApi* | [**post_v5_enterprises_enterprise_members**](docs/EnterprisesApi.md#post_v5_enterprises_enterprise_members) | **POST** /v5/enterprises/{enterprise}/members | 添加或邀请企业成员
*EnterprisesApi* | [**post_v5_enterprises_enterprise_week_report**](docs/EnterprisesApi.md#post_v5_enterprises_enterprise_week_report) | **POST** /v5/enterprises/{enterprise}/week_report | 新建周报
*EnterprisesApi* | [**post_v5_enterprises_enterprise_week_reports_id_comment**](docs/EnterprisesApi.md#post_v5_enterprises_enterprise_week_reports_id_comment) | **POST** /v5/enterprises/{enterprise}/week_reports/{id}/comment | 评论周报
*EnterprisesApi* | [**put_v5_enterprises_enterprise_members_username**](docs/EnterprisesApi.md#put_v5_enterprises_enterprise_members_username) | **PUT** /v5/enterprises/{enterprise}/members/{username} | 修改企业成员权限或备注
*GistsApi* | [**delete_v5_gists_gist_id_comments_id**](docs/GistsApi.md#delete_v5_gists_gist_id_comments_id) | **DELETE** /v5/gists/{gist_id}/comments/{id} | 删除代码片段的评论
*GistsApi* | [**delete_v5_gists_id**](docs/GistsApi.md#delete_v5_gists_id) | **DELETE** /v5/gists/{id} | 删除指定代码片段
*GistsApi* | [**delete_v5_gists_id_star**](docs/GistsApi.md#delete_v5_gists_id_star) | **DELETE** /v5/gists/{id}/star | 取消Star代码片段
*GistsApi* | [**get_v5_gists**](docs/GistsApi.md#get_v5_gists) | **GET** /v5/gists | 获取代码片段
*GistsApi* | [**get_v5_gists_gist_id_comments**](docs/GistsApi.md#get_v5_gists_gist_id_comments) | **GET** /v5/gists/{gist_id}/comments | 获取代码片段的评论
*GistsApi* | [**get_v5_gists_gist_id_comments_id**](docs/GistsApi.md#get_v5_gists_gist_id_comments_id) | **GET** /v5/gists/{gist_id}/comments/{id} | 获取单条代码片段的评论
*GistsApi* | [**get_v5_gists_id**](docs/GistsApi.md#get_v5_gists_id) | **GET** /v5/gists/{id} | 获取单条代码片段
*GistsApi* | [**get_v5_gists_id_commits**](docs/GistsApi.md#get_v5_gists_id_commits) | **GET** /v5/gists/{id}/commits | 获取代码片段的commit
*GistsApi* | [**get_v5_gists_id_forks**](docs/GistsApi.md#get_v5_gists_id_forks) | **GET** /v5/gists/{id}/forks | 获取 Fork 了指定代码片段的列表
*GistsApi* | [**get_v5_gists_id_star**](docs/GistsApi.md#get_v5_gists_id_star) | **GET** /v5/gists/{id}/star | 判断代码片段是否已Star
*GistsApi* | [**get_v5_gists_starred**](docs/GistsApi.md#get_v5_gists_starred) | **GET** /v5/gists/starred | 获取用户Star的代码片段
*GistsApi* | [**patch_v5_gists_gist_id_comments_id**](docs/GistsApi.md#patch_v5_gists_gist_id_comments_id) | **PATCH** /v5/gists/{gist_id}/comments/{id} | 修改代码片段的评论
*GistsApi* | [**patch_v5_gists_id**](docs/GistsApi.md#patch_v5_gists_id) | **PATCH** /v5/gists/{id} | 修改代码片段
*GistsApi* | [**post_v5_gists**](docs/GistsApi.md#post_v5_gists) | **POST** /v5/gists | 创建代码片段
*GistsApi* | [**post_v5_gists_gist_id_comments**](docs/GistsApi.md#post_v5_gists_gist_id_comments) | **POST** /v5/gists/{gist_id}/comments | 增加代码片段的评论
*GistsApi* | [**post_v5_gists_id_forks**](docs/GistsApi.md#post_v5_gists_id_forks) | **POST** /v5/gists/{id}/forks | Fork代码片段
*GistsApi* | [**put_v5_gists_id_star**](docs/GistsApi.md#put_v5_gists_id_star) | **PUT** /v5/gists/{id}/star | Star代码片段
*GitDataApi* | [**get_v5_repos_owner_repo_git_blobs_sha**](docs/GitDataApi.md#get_v5_repos_owner_repo_git_blobs_sha) | **GET** /v5/repos/{owner}/{repo}/git/blobs/{sha} | 获取文件Blob
*GitDataApi* | [**get_v5_repos_owner_repo_git_trees_sha**](docs/GitDataApi.md#get_v5_repos_owner_repo_git_trees_sha) | **GET** /v5/repos/{owner}/{repo}/git/trees/{sha} | 获取目录Tree
*IssuesApi* | [**delete_v5_repos_owner_repo_issues_comments_id**](docs/IssuesApi.md#delete_v5_repos_owner_repo_issues_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/issues/comments/{id} | 删除Issue某条评论
*IssuesApi* | [**get_v5_enterprises_enterprise_issues**](docs/IssuesApi.md#get_v5_enterprises_enterprise_issues) | **GET** /v5/enterprises/{enterprise}/issues | 获取某个企业的所有Issues
*IssuesApi* | [**get_v5_enterprises_enterprise_issues_number**](docs/IssuesApi.md#get_v5_enterprises_enterprise_issues_number) | **GET** /v5/enterprises/{enterprise}/issues/{number} | 获取企业的某个Issue
*IssuesApi* | [**get_v5_enterprises_enterprise_issues_number_comments**](docs/IssuesApi.md#get_v5_enterprises_enterprise_issues_number_comments) | **GET** /v5/enterprises/{enterprise}/issues/{number}/comments | 获取企业某个Issue所有评论
*IssuesApi* | [**get_v5_enterprises_enterprise_issues_number_labels**](docs/IssuesApi.md#get_v5_enterprises_enterprise_issues_number_labels) | **GET** /v5/enterprises/{enterprise}/issues/{number}/labels | 获取企业某个Issue所有标签
*IssuesApi* | [**get_v5_issues**](docs/IssuesApi.md#get_v5_issues) | **GET** /v5/issues | 获取当前授权用户的所有Issues
*IssuesApi* | [**get_v5_orgs_org_issues**](docs/IssuesApi.md#get_v5_orgs_org_issues) | **GET** /v5/orgs/{org}/issues | 获取当前用户某个组织的Issues
*IssuesApi* | [**get_v5_repos_owner_issues_number_operate_logs**](docs/IssuesApi.md#get_v5_repos_owner_issues_number_operate_logs) | **GET** /v5/repos/{owner}/issues/{number}/operate_logs | 获取某个Issue下的操作日志
*IssuesApi* | [**get_v5_repos_owner_repo_issues**](docs/IssuesApi.md#get_v5_repos_owner_repo_issues) | **GET** /v5/repos/{owner}/{repo}/issues | 仓库的所有Issues
*IssuesApi* | [**get_v5_repos_owner_repo_issues_comments**](docs/IssuesApi.md#get_v5_repos_owner_repo_issues_comments) | **GET** /v5/repos/{owner}/{repo}/issues/comments | 获取仓库所有Issue的评论
*IssuesApi* | [**get_v5_repos_owner_repo_issues_comments_id**](docs/IssuesApi.md#get_v5_repos_owner_repo_issues_comments_id) | **GET** /v5/repos/{owner}/{repo}/issues/comments/{id} | 获取仓库Issue某条评论
*IssuesApi* | [**get_v5_repos_owner_repo_issues_number**](docs/IssuesApi.md#get_v5_repos_owner_repo_issues_number) | **GET** /v5/repos/{owner}/{repo}/issues/{number} | 仓库的某个Issue
*IssuesApi* | [**get_v5_repos_owner_repo_issues_number_comments**](docs/IssuesApi.md#get_v5_repos_owner_repo_issues_number_comments) | **GET** /v5/repos/{owner}/{repo}/issues/{number}/comments | 获取仓库某个Issue所有的评论
*IssuesApi* | [**get_v5_user_issues**](docs/IssuesApi.md#get_v5_user_issues) | **GET** /v5/user/issues | 获取授权用户的所有Issues
*IssuesApi* | [**patch_v5_repos_owner_issues_number**](docs/IssuesApi.md#patch_v5_repos_owner_issues_number) | **PATCH** /v5/repos/{owner}/issues/{number} | 更新Issue
*IssuesApi* | [**patch_v5_repos_owner_repo_issues_comments_id**](docs/IssuesApi.md#patch_v5_repos_owner_repo_issues_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/issues/comments/{id} | 更新Issue某条评论
*IssuesApi* | [**post_v5_repos_owner_issues**](docs/IssuesApi.md#post_v5_repos_owner_issues) | **POST** /v5/repos/{owner}/issues | 创建Issue
*IssuesApi* | [**post_v5_repos_owner_repo_issues_number_comments**](docs/IssuesApi.md#post_v5_repos_owner_repo_issues_number_comments) | **POST** /v5/repos/{owner}/{repo}/issues/{number}/comments | 创建某个Issue评论
*LabelsApi* | [**delete_v5_repos_owner_repo_issues_number_labels**](docs/LabelsApi.md#delete_v5_repos_owner_repo_issues_number_labels) | **DELETE** /v5/repos/{owner}/{repo}/issues/{number}/labels | 删除Issue所有标签
*LabelsApi* | [**delete_v5_repos_owner_repo_issues_number_labels_name**](docs/LabelsApi.md#delete_v5_repos_owner_repo_issues_number_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/issues/{number}/labels/{name} | 删除Issue标签
*LabelsApi* | [**delete_v5_repos_owner_repo_labels_name**](docs/LabelsApi.md#delete_v5_repos_owner_repo_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/labels/{name} | 删除一个仓库任务标签
*LabelsApi* | [**get_v5_enterprises_enterprise_labels**](docs/LabelsApi.md#get_v5_enterprises_enterprise_labels) | **GET** /v5/enterprises/{enterprise}/labels | 获取企业所有标签
*LabelsApi* | [**get_v5_enterprises_enterprise_labels_name**](docs/LabelsApi.md#get_v5_enterprises_enterprise_labels_name) | **GET** /v5/enterprises/{enterprise}/labels/{name} | 获取企业某个标签
*LabelsApi* | [**get_v5_repos_owner_repo_issues_number_labels**](docs/LabelsApi.md#get_v5_repos_owner_repo_issues_number_labels) | **GET** /v5/repos/{owner}/{repo}/issues/{number}/labels | 获取仓库任务的所有标签
*LabelsApi* | [**get_v5_repos_owner_repo_labels**](docs/LabelsApi.md#get_v5_repos_owner_repo_labels) | **GET** /v5/repos/{owner}/{repo}/labels | 获取仓库所有任务标签
*LabelsApi* | [**get_v5_repos_owner_repo_labels_name**](docs/LabelsApi.md#get_v5_repos_owner_repo_labels_name) | **GET** /v5/repos/{owner}/{repo}/labels/{name} | 根据标签名称获取单个标签
*LabelsApi* | [**patch_v5_repos_owner_repo_labels_original_name**](docs/LabelsApi.md#patch_v5_repos_owner_repo_labels_original_name) | **PATCH** /v5/repos/{owner}/{repo}/labels/{original_name} | 更新一个仓库任务标签
*LabelsApi* | [**post_v5_repos_owner_repo_issues_number_labels**](docs/LabelsApi.md#post_v5_repos_owner_repo_issues_number_labels) | **POST** /v5/repos/{owner}/{repo}/issues/{number}/labels | 创建Issue标签
*LabelsApi* | [**post_v5_repos_owner_repo_labels**](docs/LabelsApi.md#post_v5_repos_owner_repo_labels) | **POST** /v5/repos/{owner}/{repo}/labels | 创建仓库任务标签
*LabelsApi* | [**put_v5_repos_owner_repo_issues_number_labels**](docs/LabelsApi.md#put_v5_repos_owner_repo_issues_number_labels) | **PUT** /v5/repos/{owner}/{repo}/issues/{number}/labels | 替换Issue所有标签
*MilestonesApi* | [**delete_v5_repos_owner_repo_milestones_number**](docs/MilestonesApi.md#delete_v5_repos_owner_repo_milestones_number) | **DELETE** /v5/repos/{owner}/{repo}/milestones/{number} | 删除仓库单个里程碑
*MilestonesApi* | [**get_v5_repos_owner_repo_milestones**](docs/MilestonesApi.md#get_v5_repos_owner_repo_milestones) | **GET** /v5/repos/{owner}/{repo}/milestones | 获取仓库所有里程碑
*MilestonesApi* | [**get_v5_repos_owner_repo_milestones_number**](docs/MilestonesApi.md#get_v5_repos_owner_repo_milestones_number) | **GET** /v5/repos/{owner}/{repo}/milestones/{number} | 获取仓库单个里程碑
*MilestonesApi* | [**patch_v5_repos_owner_repo_milestones_number**](docs/MilestonesApi.md#patch_v5_repos_owner_repo_milestones_number) | **PATCH** /v5/repos/{owner}/{repo}/milestones/{number} | 更新仓库里程碑
*MilestonesApi* | [**post_v5_repos_owner_repo_milestones**](docs/MilestonesApi.md#post_v5_repos_owner_repo_milestones) | **POST** /v5/repos/{owner}/{repo}/milestones | 创建仓库里程碑
*MiscellaneousApi* | [**get_v5_emojis**](docs/MiscellaneousApi.md#get_v5_emojis) | **GET** /v5/emojis | 列出可使用的 Emoji
*MiscellaneousApi* | [**get_v5_gitignore_templates**](docs/MiscellaneousApi.md#get_v5_gitignore_templates) | **GET** /v5/gitignore/templates | 列出可使用的 .gitignore 模板
*MiscellaneousApi* | [**get_v5_gitignore_templates_name**](docs/MiscellaneousApi.md#get_v5_gitignore_templates_name) | **GET** /v5/gitignore/templates/{name} | 获取一个 .gitignore 模板
*MiscellaneousApi* | [**get_v5_gitignore_templates_name_raw**](docs/MiscellaneousApi.md#get_v5_gitignore_templates_name_raw) | **GET** /v5/gitignore/templates/{name}/raw | 获取一个 .gitignore 模板原始文件
*MiscellaneousApi* | [**get_v5_licenses**](docs/MiscellaneousApi.md#get_v5_licenses) | **GET** /v5/licenses | 列出可使用的开源许可协议
*MiscellaneousApi* | [**get_v5_licenses_license**](docs/MiscellaneousApi.md#get_v5_licenses_license) | **GET** /v5/licenses/{license} | 获取一个开源许可协议
*MiscellaneousApi* | [**get_v5_licenses_license_raw**](docs/MiscellaneousApi.md#get_v5_licenses_license_raw) | **GET** /v5/licenses/{license}/raw | 获取一个开源许可协议原始文件
*MiscellaneousApi* | [**get_v5_repos_owner_repo_license**](docs/MiscellaneousApi.md#get_v5_repos_owner_repo_license) | **GET** /v5/repos/{owner}/{repo}/license | 获取一个仓库使用的开源许可协议
*MiscellaneousApi* | [**post_v5_markdown**](docs/MiscellaneousApi.md#post_v5_markdown) | **POST** /v5/markdown | 渲染 Markdown 文本
*OrganizationsApi* | [**delete_v5_orgs_org_memberships_username**](docs/OrganizationsApi.md#delete_v5_orgs_org_memberships_username) | **DELETE** /v5/orgs/{org}/memberships/{username} | 移除授权用户所管理组织中的成员
*OrganizationsApi* | [**delete_v5_user_memberships_orgs_org**](docs/OrganizationsApi.md#delete_v5_user_memberships_orgs_org) | **DELETE** /v5/user/memberships/orgs/{org} | 退出一个组织
*OrganizationsApi* | [**get_v5_orgs_org**](docs/OrganizationsApi.md#get_v5_orgs_org) | **GET** /v5/orgs/{org} | 获取一个组织
*OrganizationsApi* | [**get_v5_orgs_org_followers**](docs/OrganizationsApi.md#get_v5_orgs_org_followers) | **GET** /v5/orgs/{org}/followers | 列出指定组织的所有关注者
*OrganizationsApi* | [**get_v5_orgs_org_members**](docs/OrganizationsApi.md#get_v5_orgs_org_members) | **GET** /v5/orgs/{org}/members | 列出一个组织的所有成员
*OrganizationsApi* | [**get_v5_orgs_org_memberships_username**](docs/OrganizationsApi.md#get_v5_orgs_org_memberships_username) | **GET** /v5/orgs/{org}/memberships/{username} | 获取授权用户所属组织的一个成员
*OrganizationsApi* | [**get_v5_user_memberships_orgs**](docs/OrganizationsApi.md#get_v5_user_memberships_orgs) | **GET** /v5/user/memberships/orgs | 列出授权用户在所属组织的成员资料
*OrganizationsApi* | [**get_v5_user_memberships_orgs_org**](docs/OrganizationsApi.md#get_v5_user_memberships_orgs_org) | **GET** /v5/user/memberships/orgs/{org} | 获取授权用户在一个组织的成员资料
*OrganizationsApi* | [**get_v5_user_orgs**](docs/OrganizationsApi.md#get_v5_user_orgs) | **GET** /v5/user/orgs | 列出授权用户所属的组织
*OrganizationsApi* | [**get_v5_users_username_orgs**](docs/OrganizationsApi.md#get_v5_users_username_orgs) | **GET** /v5/users/{username}/orgs | 列出用户所属的组织
*OrganizationsApi* | [**patch_v5_orgs_org**](docs/OrganizationsApi.md#patch_v5_orgs_org) | **PATCH** /v5/orgs/{org} | 更新授权用户所管理的组织资料
*OrganizationsApi* | [**patch_v5_user_memberships_orgs_org**](docs/OrganizationsApi.md#patch_v5_user_memberships_orgs_org) | **PATCH** /v5/user/memberships/orgs/{org} | 更新授权用户在一个组织的成员资料
*OrganizationsApi* | [**post_v5_users_organization**](docs/OrganizationsApi.md#post_v5_users_organization) | **POST** /v5/users/organization | 创建组织
*OrganizationsApi* | [**put_v5_orgs_org_memberships_username**](docs/OrganizationsApi.md#put_v5_orgs_org_memberships_username) | **PUT** /v5/orgs/{org}/memberships/{username} | 增加或更新授权用户所管理组织的成员
*PullRequestsApi* | [**delete_v5_repos_owner_repo_pulls_comments_id**](docs/PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 删除评论
*PullRequestsApi* | [**delete_v5_repos_owner_repo_pulls_number_assignees**](docs/PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_assignees) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 取消用户审查 Pull Request
*PullRequestsApi* | [**delete_v5_repos_owner_repo_pulls_number_labels_name**](docs/PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/labels/{name} | 删除 Pull Request 标签
*PullRequestsApi* | [**delete_v5_repos_owner_repo_pulls_number_testers**](docs/PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_testers) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 取消用户测试 Pull Request
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls) | **GET** /v5/repos/{owner}/{repo}/pulls | 获取Pull Request列表
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_comments**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_comments) | **GET** /v5/repos/{owner}/{repo}/pulls/comments | 获取该仓库下的所有Pull Request评论
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_comments_id**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_comments_id) | **GET** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 获取Pull Request的某个评论
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number) | **GET** /v5/repos/{owner}/{repo}/pulls/{number} | 获取单个Pull Request
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_comments**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_comments) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/comments | 获取某个Pull Request的所有评论
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_commits**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_commits) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/commits | 获取某Pull Request的所有Commit信息。最多显示250条Commit
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_files**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_files) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/files | Pull Request Commit文件列表。最多显示300条diff
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_issues**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_issues) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/issues | 获取 Pull Request 关联的 issues
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_labels**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_labels) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 获取某个 Pull Request 的所有标签
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_merge**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_merge) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/merge | 判断Pull Request是否已经合并
*PullRequestsApi* | [**get_v5_repos_owner_repo_pulls_number_operate_logs**](docs/PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_operate_logs) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/operate_logs | 获取某个Pull Request的操作日志
*PullRequestsApi* | [**patch_v5_repos_owner_repo_pulls_comments_id**](docs/PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 编辑评论
*PullRequestsApi* | [**patch_v5_repos_owner_repo_pulls_number**](docs/PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number} | 更新Pull Request信息
*PullRequestsApi* | [**patch_v5_repos_owner_repo_pulls_number_assignees**](docs/PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number_assignees) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 重置 Pull Request 审查 的状态
*PullRequestsApi* | [**patch_v5_repos_owner_repo_pulls_number_testers**](docs/PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number_testers) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 重置 Pull Request 测试 的状态
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls) | **POST** /v5/repos/{owner}/{repo}/pulls | 创建Pull Request
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_assignees**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_assignees) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 指派用户审查 Pull Request
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_comments**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_comments) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/comments | 提交Pull Request评论
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_labels**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_labels) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 创建 Pull Request 标签
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_review**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_review) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/review | 处理 Pull Request 审查
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_test**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_test) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/test | 处理 Pull Request 测试
*PullRequestsApi* | [**post_v5_repos_owner_repo_pulls_number_testers**](docs/PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_testers) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 指派用户测试 Pull Request
*PullRequestsApi* | [**put_v5_repos_owner_repo_pulls_number_labels**](docs/PullRequestsApi.md#put_v5_repos_owner_repo_pulls_number_labels) | **PUT** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 替换 Pull Request 所有标签
*PullRequestsApi* | [**put_v5_repos_owner_repo_pulls_number_merge**](docs/PullRequestsApi.md#put_v5_repos_owner_repo_pulls_number_merge) | **PUT** /v5/repos/{owner}/{repo}/pulls/{number}/merge | 合并Pull Request
*RepositoriesApi* | [**delete_v5_repos_owner_repo**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo) | **DELETE** /v5/repos/{owner}/{repo} | 删除一个仓库
*RepositoriesApi* | [**delete_v5_repos_owner_repo_branches_branch_protection**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_branches_branch_protection) | **DELETE** /v5/repos/{owner}/{repo}/branches/{branch}/protection | 取消保护分支的设置
*RepositoriesApi* | [**delete_v5_repos_owner_repo_collaborators_username**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_collaborators_username) | **DELETE** /v5/repos/{owner}/{repo}/collaborators/{username} | 移除仓库成员
*RepositoriesApi* | [**delete_v5_repos_owner_repo_comments_id**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/comments/{id} | 删除Commit评论
*RepositoriesApi* | [**delete_v5_repos_owner_repo_contents_path**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_contents_path) | **DELETE** /v5/repos/{owner}/{repo}/contents/{path} | 删除文件
*RepositoriesApi* | [**delete_v5_repos_owner_repo_keys_enable_id**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_keys_enable_id) | **DELETE** /v5/repos/{owner}/{repo}/keys/enable/{id} | 停用仓库公钥
*RepositoriesApi* | [**delete_v5_repos_owner_repo_keys_id**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_keys_id) | **DELETE** /v5/repos/{owner}/{repo}/keys/{id} | 删除一个仓库公钥
*RepositoriesApi* | [**delete_v5_repos_owner_repo_releases_id**](docs/RepositoriesApi.md#delete_v5_repos_owner_repo_releases_id) | **DELETE** /v5/repos/{owner}/{repo}/releases/{id} | 删除仓库Release
*RepositoriesApi* | [**get_v5_enterprises_enterprise_repos**](docs/RepositoriesApi.md#get_v5_enterprises_enterprise_repos) | **GET** /v5/enterprises/{enterprise}/repos | 获取企业的所有仓库
*RepositoriesApi* | [**get_v5_orgs_org_repos**](docs/RepositoriesApi.md#get_v5_orgs_org_repos) | **GET** /v5/orgs/{org}/repos | 获取一个组织的仓库
*RepositoriesApi* | [**get_v5_repos_owner_repo**](docs/RepositoriesApi.md#get_v5_repos_owner_repo) | **GET** /v5/repos/{owner}/{repo} | 获取用户的某个仓库
*RepositoriesApi* | [**get_v5_repos_owner_repo_branches**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_branches) | **GET** /v5/repos/{owner}/{repo}/branches | 获取所有分支
*RepositoriesApi* | [**get_v5_repos_owner_repo_branches_branch**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_branches_branch) | **GET** /v5/repos/{owner}/{repo}/branches/{branch} | 获取单个分支
*RepositoriesApi* | [**get_v5_repos_owner_repo_collaborators**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_collaborators) | **GET** /v5/repos/{owner}/{repo}/collaborators | 获取仓库的所有成员
*RepositoriesApi* | [**get_v5_repos_owner_repo_collaborators_username**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_collaborators_username) | **GET** /v5/repos/{owner}/{repo}/collaborators/{username} | 判断用户是否为仓库成员
*RepositoriesApi* | [**get_v5_repos_owner_repo_collaborators_username_permission**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_collaborators_username_permission) | **GET** /v5/repos/{owner}/{repo}/collaborators/{username}/permission | 查看仓库成员的权限
*RepositoriesApi* | [**get_v5_repos_owner_repo_comments**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_comments) | **GET** /v5/repos/{owner}/{repo}/comments | 获取仓库的Commit评论
*RepositoriesApi* | [**get_v5_repos_owner_repo_comments_id**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_comments_id) | **GET** /v5/repos/{owner}/{repo}/comments/{id} | 获取仓库的某条Commit评论
*RepositoriesApi* | [**get_v5_repos_owner_repo_commits**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_commits) | **GET** /v5/repos/{owner}/{repo}/commits | 仓库的所有提交
*RepositoriesApi* | [**get_v5_repos_owner_repo_commits_ref_comments**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_commits_ref_comments) | **GET** /v5/repos/{owner}/{repo}/commits/{ref}/comments | 获取单个Commit的评论
*RepositoriesApi* | [**get_v5_repos_owner_repo_commits_sha**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_commits_sha) | **GET** /v5/repos/{owner}/{repo}/commits/{sha} | 仓库的某个提交
*RepositoriesApi* | [**get_v5_repos_owner_repo_compare_base___head**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_compare_base___head) | **GET** /v5/repos/{owner}/{repo}/compare/{base}...{head} | 两个Commits之间对比的版本差异
*RepositoriesApi* | [**get_v5_repos_owner_repo_contents_path**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_contents_path) | **GET** /v5/repos/{owner}/{repo}/contents(/{path}) | 获取仓库具体路径下的内容
*RepositoriesApi* | [**get_v5_repos_owner_repo_contributors**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_contributors) | **GET** /v5/repos/{owner}/{repo}/contributors | 获取仓库贡献者
*RepositoriesApi* | [**get_v5_repos_owner_repo_forks**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_forks) | **GET** /v5/repos/{owner}/{repo}/forks | 查看仓库的Forks
*RepositoriesApi* | [**get_v5_repos_owner_repo_keys**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_keys) | **GET** /v5/repos/{owner}/{repo}/keys | 获取仓库已部署的公钥
*RepositoriesApi* | [**get_v5_repos_owner_repo_keys_available**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_keys_available) | **GET** /v5/repos/{owner}/{repo}/keys/available | 获取仓库可部署的公钥
*RepositoriesApi* | [**get_v5_repos_owner_repo_keys_id**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_keys_id) | **GET** /v5/repos/{owner}/{repo}/keys/{id} | 获取仓库的单个公钥
*RepositoriesApi* | [**get_v5_repos_owner_repo_pages**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_pages) | **GET** /v5/repos/{owner}/{repo}/pages | 获取Pages信息
*RepositoriesApi* | [**get_v5_repos_owner_repo_readme**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_readme) | **GET** /v5/repos/{owner}/{repo}/readme | 获取仓库README
*RepositoriesApi* | [**get_v5_repos_owner_repo_releases**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_releases) | **GET** /v5/repos/{owner}/{repo}/releases | 获取仓库的所有Releases
*RepositoriesApi* | [**get_v5_repos_owner_repo_releases_id**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_releases_id) | **GET** /v5/repos/{owner}/{repo}/releases/{id} | 获取仓库的单个Releases
*RepositoriesApi* | [**get_v5_repos_owner_repo_releases_latest**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_releases_latest) | **GET** /v5/repos/{owner}/{repo}/releases/latest | 获取仓库的最后更新的Release
*RepositoriesApi* | [**get_v5_repos_owner_repo_releases_tags_tag**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_releases_tags_tag) | **GET** /v5/repos/{owner}/{repo}/releases/tags/{tag} | 根据Tag名称获取仓库的Release
*RepositoriesApi* | [**get_v5_repos_owner_repo_tags**](docs/RepositoriesApi.md#get_v5_repos_owner_repo_tags) | **GET** /v5/repos/{owner}/{repo}/tags | 列出仓库所有的tags
*RepositoriesApi* | [**get_v5_user_repos**](docs/RepositoriesApi.md#get_v5_user_repos) | **GET** /v5/user/repos | 列出授权用户的所有仓库
*RepositoriesApi* | [**get_v5_users_username_repos**](docs/RepositoriesApi.md#get_v5_users_username_repos) | **GET** /v5/users/{username}/repos | 获取某个用户的公开仓库
*RepositoriesApi* | [**patch_v5_repos_owner_repo**](docs/RepositoriesApi.md#patch_v5_repos_owner_repo) | **PATCH** /v5/repos/{owner}/{repo} | 更新仓库设置
*RepositoriesApi* | [**patch_v5_repos_owner_repo_comments_id**](docs/RepositoriesApi.md#patch_v5_repos_owner_repo_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/comments/{id} | 更新Commit评论
*RepositoriesApi* | [**patch_v5_repos_owner_repo_releases_id**](docs/RepositoriesApi.md#patch_v5_repos_owner_repo_releases_id) | **PATCH** /v5/repos/{owner}/{repo}/releases/{id} | 更新仓库Release
*RepositoriesApi* | [**post_v5_enterprises_enterprise_repos**](docs/RepositoriesApi.md#post_v5_enterprises_enterprise_repos) | **POST** /v5/enterprises/{enterprise}/repos | 创建企业仓库
*RepositoriesApi* | [**post_v5_orgs_org_repos**](docs/RepositoriesApi.md#post_v5_orgs_org_repos) | **POST** /v5/orgs/{org}/repos | 创建组织仓库
*RepositoriesApi* | [**post_v5_repos_owner_repo_branches**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_branches) | **POST** /v5/repos/{owner}/{repo}/branches | 创建分支
*RepositoriesApi* | [**post_v5_repos_owner_repo_commits_sha_comments**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_commits_sha_comments) | **POST** /v5/repos/{owner}/{repo}/commits/{sha}/comments | 创建Commit评论
*RepositoriesApi* | [**post_v5_repos_owner_repo_contents_path**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_contents_path) | **POST** /v5/repos/{owner}/{repo}/contents/{path} | 新建文件
*RepositoriesApi* | [**post_v5_repos_owner_repo_forks**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_forks) | **POST** /v5/repos/{owner}/{repo}/forks | Fork一个仓库
*RepositoriesApi* | [**post_v5_repos_owner_repo_keys**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_keys) | **POST** /v5/repos/{owner}/{repo}/keys | 为仓库添加公钥
*RepositoriesApi* | [**post_v5_repos_owner_repo_pages_builds**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_pages_builds) | **POST** /v5/repos/{owner}/{repo}/pages/builds | 请求建立Pages
*RepositoriesApi* | [**post_v5_repos_owner_repo_releases**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_releases) | **POST** /v5/repos/{owner}/{repo}/releases | 创建仓库Release
*RepositoriesApi* | [**post_v5_repos_owner_repo_tags**](docs/RepositoriesApi.md#post_v5_repos_owner_repo_tags) | **POST** /v5/repos/{owner}/{repo}/tags | 创建一个仓库的 Tag
*RepositoriesApi* | [**post_v5_user_repos**](docs/RepositoriesApi.md#post_v5_user_repos) | **POST** /v5/user/repos | 创建一个仓库
*RepositoriesApi* | [**put_v5_repos_owner_repo_branches_branch_protection**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_branches_branch_protection) | **PUT** /v5/repos/{owner}/{repo}/branches/{branch}/protection | 设置分支保护
*RepositoriesApi* | [**put_v5_repos_owner_repo_clear**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_clear) | **PUT** /v5/repos/{owner}/{repo}/clear | 清空一个仓库
*RepositoriesApi* | [**put_v5_repos_owner_repo_collaborators_username**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_collaborators_username) | **PUT** /v5/repos/{owner}/{repo}/collaborators/{username} | 添加仓库成员
*RepositoriesApi* | [**put_v5_repos_owner_repo_contents_path**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_contents_path) | **PUT** /v5/repos/{owner}/{repo}/contents/{path} | 更新文件
*RepositoriesApi* | [**put_v5_repos_owner_repo_keys_enable_id**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_keys_enable_id) | **PUT** /v5/repos/{owner}/{repo}/keys/enable/{id} | 启用仓库公钥
*RepositoriesApi* | [**put_v5_repos_owner_repo_reviewer**](docs/RepositoriesApi.md#put_v5_repos_owner_repo_reviewer) | **PUT** /v5/repos/{owner}/{repo}/reviewer | 修改代码审查设置
*SearchApi* | [**get_v5_search_issues**](docs/SearchApi.md#get_v5_search_issues) | **GET** /v5/search/issues | 搜索 Issues
*SearchApi* | [**get_v5_search_repositories**](docs/SearchApi.md#get_v5_search_repositories) | **GET** /v5/search/repositories | 搜索仓库
*SearchApi* | [**get_v5_search_users**](docs/SearchApi.md#get_v5_search_users) | **GET** /v5/search/users | 搜索用户
*UsersApi* | [**delete_v5_user_following_username**](docs/UsersApi.md#delete_v5_user_following_username) | **DELETE** /v5/user/following/{username} | 取消关注一个用户
*UsersApi* | [**delete_v5_user_keys_id**](docs/UsersApi.md#delete_v5_user_keys_id) | **DELETE** /v5/user/keys/{id} | 删除一个公钥
*UsersApi* | [**get_v5_user**](docs/UsersApi.md#get_v5_user) | **GET** /v5/user | 获取授权用户的资料
*UsersApi* | [**get_v5_user_followers**](docs/UsersApi.md#get_v5_user_followers) | **GET** /v5/user/followers | 列出授权用户的关注者
*UsersApi* | [**get_v5_user_following**](docs/UsersApi.md#get_v5_user_following) | **GET** /v5/user/following | 列出授权用户正关注的用户
*UsersApi* | [**get_v5_user_following_username**](docs/UsersApi.md#get_v5_user_following_username) | **GET** /v5/user/following/{username} | 检查授权用户是否关注了一个用户
*UsersApi* | [**get_v5_user_keys**](docs/UsersApi.md#get_v5_user_keys) | **GET** /v5/user/keys | 列出授权用户的所有公钥
*UsersApi* | [**get_v5_user_keys_id**](docs/UsersApi.md#get_v5_user_keys_id) | **GET** /v5/user/keys/{id} | 获取一个公钥
*UsersApi* | [**get_v5_user_namespace**](docs/UsersApi.md#get_v5_user_namespace) | **GET** /v5/user/namespace | 获取授权用户的一个 Namespace
*UsersApi* | [**get_v5_user_namespaces**](docs/UsersApi.md#get_v5_user_namespaces) | **GET** /v5/user/namespaces | 列出授权用户所有的 Namespace
*UsersApi* | [**get_v5_users_username**](docs/UsersApi.md#get_v5_users_username) | **GET** /v5/users/{username} | 获取一个用户
*UsersApi* | [**get_v5_users_username_followers**](docs/UsersApi.md#get_v5_users_username_followers) | **GET** /v5/users/{username}/followers | 列出指定用户的关注者
*UsersApi* | [**get_v5_users_username_following**](docs/UsersApi.md#get_v5_users_username_following) | **GET** /v5/users/{username}/following | 列出指定用户正在关注的用户
*UsersApi* | [**get_v5_users_username_following_target_user**](docs/UsersApi.md#get_v5_users_username_following_target_user) | **GET** /v5/users/{username}/following/{target_user} | 检查指定用户是否关注目标用户
*UsersApi* | [**get_v5_users_username_keys**](docs/UsersApi.md#get_v5_users_username_keys) | **GET** /v5/users/{username}/keys | 列出指定用户的所有公钥
*UsersApi* | [**patch_v5_user**](docs/UsersApi.md#patch_v5_user) | **PATCH** /v5/user | 更新授权用户的资料
*UsersApi* | [**post_v5_user_keys**](docs/UsersApi.md#post_v5_user_keys) | **POST** /v5/user/keys | 添加一个公钥
*UsersApi* | [**put_v5_user_following_username**](docs/UsersApi.md#put_v5_user_following_username) | **PUT** /v5/user/following/{username} | 关注一个用户
*WebhooksApi* | [**delete_v5_repos_owner_repo_hooks_id**](docs/WebhooksApi.md#delete_v5_repos_owner_repo_hooks_id) | **DELETE** /v5/repos/{owner}/{repo}/hooks/{id} | 删除一个仓库WebHook
*WebhooksApi* | [**get_v5_repos_owner_repo_hooks**](docs/WebhooksApi.md#get_v5_repos_owner_repo_hooks) | **GET** /v5/repos/{owner}/{repo}/hooks | 列出仓库的WebHooks
*WebhooksApi* | [**get_v5_repos_owner_repo_hooks_id**](docs/WebhooksApi.md#get_v5_repos_owner_repo_hooks_id) | **GET** /v5/repos/{owner}/{repo}/hooks/{id} | 获取仓库单个WebHook
*WebhooksApi* | [**patch_v5_repos_owner_repo_hooks_id**](docs/WebhooksApi.md#patch_v5_repos_owner_repo_hooks_id) | **PATCH** /v5/repos/{owner}/{repo}/hooks/{id} | 更新一个仓库WebHook
*WebhooksApi* | [**post_v5_repos_owner_repo_hooks**](docs/WebhooksApi.md#post_v5_repos_owner_repo_hooks) | **POST** /v5/repos/{owner}/{repo}/hooks | 创建一个仓库WebHook
*WebhooksApi* | [**post_v5_repos_owner_repo_hooks_id_tests**](docs/WebhooksApi.md#post_v5_repos_owner_repo_hooks_id_tests) | **POST** /v5/repos/{owner}/{repo}/hooks/{id}/tests | 测试WebHook是否发送成功

## Documentation For Models

 - [Blob](docs/Blob.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body10](docs/Body10.md)
 - [Body11](docs/Body11.md)
 - [Body12](docs/Body12.md)
 - [Body13](docs/Body13.md)
 - [Body14](docs/Body14.md)
 - [Body15](docs/Body15.md)
 - [Body16](docs/Body16.md)
 - [Body17](docs/Body17.md)
 - [Body18](docs/Body18.md)
 - [Body19](docs/Body19.md)
 - [Body2](docs/Body2.md)
 - [Body20](docs/Body20.md)
 - [Body21](docs/Body21.md)
 - [Body22](docs/Body22.md)
 - [Body23](docs/Body23.md)
 - [Body24](docs/Body24.md)
 - [Body25](docs/Body25.md)
 - [Body26](docs/Body26.md)
 - [Body27](docs/Body27.md)
 - [Body28](docs/Body28.md)
 - [Body29](docs/Body29.md)
 - [Body3](docs/Body3.md)
 - [Body30](docs/Body30.md)
 - [Body31](docs/Body31.md)
 - [Body32](docs/Body32.md)
 - [Body33](docs/Body33.md)
 - [Body34](docs/Body34.md)
 - [Body35](docs/Body35.md)
 - [Body36](docs/Body36.md)
 - [Body37](docs/Body37.md)
 - [Body38](docs/Body38.md)
 - [Body39](docs/Body39.md)
 - [Body4](docs/Body4.md)
 - [Body40](docs/Body40.md)
 - [Body41](docs/Body41.md)
 - [Body42](docs/Body42.md)
 - [Body43](docs/Body43.md)
 - [Body44](docs/Body44.md)
 - [Body45](docs/Body45.md)
 - [Body46](docs/Body46.md)
 - [Body47](docs/Body47.md)
 - [Body48](docs/Body48.md)
 - [Body49](docs/Body49.md)
 - [Body5](docs/Body5.md)
 - [Body50](docs/Body50.md)
 - [Body51](docs/Body51.md)
 - [Body52](docs/Body52.md)
 - [Body53](docs/Body53.md)
 - [Body54](docs/Body54.md)
 - [Body55](docs/Body55.md)
 - [Body56](docs/Body56.md)
 - [Body57](docs/Body57.md)
 - [Body58](docs/Body58.md)
 - [Body59](docs/Body59.md)
 - [Body6](docs/Body6.md)
 - [Body60](docs/Body60.md)
 - [Body61](docs/Body61.md)
 - [Body62](docs/Body62.md)
 - [Body63](docs/Body63.md)
 - [Body64](docs/Body64.md)
 - [Body65](docs/Body65.md)
 - [Body66](docs/Body66.md)
 - [Body67](docs/Body67.md)
 - [Body68](docs/Body68.md)
 - [Body69](docs/Body69.md)
 - [Body7](docs/Body7.md)
 - [Body70](docs/Body70.md)
 - [Body71](docs/Body71.md)
 - [Body72](docs/Body72.md)
 - [Body8](docs/Body8.md)
 - [Body9](docs/Body9.md)
 - [Branch](docs/Branch.md)
 - [Code](docs/Code.md)
 - [CodeComment](docs/CodeComment.md)
 - [CodeForks](docs/CodeForks.md)
 - [CodeForksHistory](docs/CodeForksHistory.md)
 - [Commit](docs/Commit.md)
 - [CommitContent](docs/CommitContent.md)
 - [Compare](docs/Compare.md)
 - [CompleteBranch](docs/CompleteBranch.md)
 - [Content](docs/Content.md)
 - [ContentBasic](docs/ContentBasic.md)
 - [Contributor](docs/Contributor.md)
 - [EnterpriseBasic](docs/EnterpriseBasic.md)
 - [EnterpriseMember](docs/EnterpriseMember.md)
 - [Event](docs/Event.md)
 - [Group](docs/Group.md)
 - [GroupDetail](docs/GroupDetail.md)
 - [GroupFollowers](docs/GroupFollowers.md)
 - [GroupMember](docs/GroupMember.md)
 - [Hook](docs/Hook.md)
 - [Issue](docs/Issue.md)
 - [Label](docs/Label.md)
 - [Milestone](docs/Milestone.md)
 - [Namespace](docs/Namespace.md)
 - [NamespaceMini](docs/NamespaceMini.md)
 - [Note](docs/Note.md)
 - [OperateLog](docs/OperateLog.md)
 - [ProgramBasic](docs/ProgramBasic.md)
 - [Project](docs/Project.md)
 - [ProjectBasic](docs/ProjectBasic.md)
 - [ProjectMember](docs/ProjectMember.md)
 - [ProjectMemberPermission](docs/ProjectMemberPermission.md)
 - [ProjectStargazers](docs/ProjectStargazers.md)
 - [ProjectWatchers](docs/ProjectWatchers.md)
 - [PullRequest](docs/PullRequest.md)
 - [PullRequestComments](docs/PullRequestComments.md)
 - [PullRequestCommits](docs/PullRequestCommits.md)
 - [PullRequestFiles](docs/PullRequestFiles.md)
 - [Release](docs/Release.md)
 - [RepoCommit](docs/RepoCommit.md)
 - [SSHKey](docs/SSHKey.md)
 - [SSHKeyBasic](docs/SSHKeyBasic.md)
 - [Tag](docs/Tag.md)
 - [Tree](docs/Tree.md)
 - [User](docs/User.md)
 - [UserBasic](docs/UserBasic.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserEmail](docs/UserEmail.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserMessage](docs/UserMessage.md)
 - [UserMessageList](docs/UserMessageList.md)
 - [UserMini](docs/UserMini.md)
 - [UserNotification](docs/UserNotification.md)
 - [UserNotificationCount](docs/UserNotificationCount.md)
 - [UserNotificationList](docs/UserNotificationList.md)
 - [UserNotificationNamespace](docs/UserNotificationNamespace.md)
 - [UserNotificationSubject](docs/UserNotificationSubject.md)
 - [WeekReport](docs/WeekReport.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

kingreatwill

codegen 3.0.21
