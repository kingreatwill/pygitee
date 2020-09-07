# coding: utf-8


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gitee.api_client import ApiClient


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_v5_repos_owner_repo_hooks_id(self, owner, repo, id, **kwargs):  # noqa: E501
        """删除一个仓库WebHook  # noqa: E501

        删除一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v5_repos_owner_repo_hooks_id(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
            return data

    def delete_v5_repos_owner_repo_hooks_id_with_http_info(self, owner, repo, id, **kwargs):  # noqa: E501
        """删除一个仓库WebHook  # noqa: E501

        删除一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_v5_repos_owner_repo_hooks_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `delete_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `delete_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_v5_repos_owner_repo_hooks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_repos_owner_repo_hooks(self, owner, repo, **kwargs):  # noqa: E501
        """列出仓库的WebHooks  # noqa: E501

        列出仓库的WebHooks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_hooks(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: list[Hook]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_repos_owner_repo_hooks_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_repos_owner_repo_hooks_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def get_v5_repos_owner_repo_hooks_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """列出仓库的WebHooks  # noqa: E501

        列出仓库的WebHooks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_hooks_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: list[Hook]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'access_token', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_repos_owner_repo_hooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `get_v5_repos_owner_repo_hooks`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `get_v5_repos_owner_repo_hooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Hook]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v5_repos_owner_repo_hooks_id(self, owner, repo, id, **kwargs):  # noqa: E501
        """获取仓库单个WebHook  # noqa: E501

        获取仓库单个WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_hooks_id(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param str access_token: 用户授权码
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
            return data

    def get_v5_repos_owner_repo_hooks_id_with_http_info(self, owner, repo, id, **kwargs):  # noqa: E501
        """获取仓库单个WebHook  # noqa: E501

        获取仓库单个WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v5_repos_owner_repo_hooks_id_with_http_info(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param str access_token: 用户授权码
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v5_repos_owner_repo_hooks_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `get_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `get_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `get_v5_repos_owner_repo_hooks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Hook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_v5_repos_owner_repo_hooks_id(self, access_token, url, password, push_events, tag_push_events,
                                           issues_events, note_events, merge_requests_events, owner, repo, id,
                                           **kwargs):  # noqa: E501
        """更新一个仓库WebHook  # noqa: E501

        更新一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_v5_repos_owner_repo_hooks_id(access_token, url, password, push_events, tag_push_events, issues_events, note_events, merge_requests_events, owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: (required)
        :param str url: (required)
        :param str password: (required)
        :param bool push_events: (required)
        :param bool tag_push_events: (required)
        :param bool issues_events: (required)
        :param bool note_events: (required)
        :param bool merge_requests_events: (required)
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_v5_repos_owner_repo_hooks_id_with_http_info(access_token, url, password, push_events,
                                                                          tag_push_events, issues_events, note_events,
                                                                          merge_requests_events, owner, repo, id,
                                                                          **kwargs)  # noqa: E501
        else:
            (data) = self.patch_v5_repos_owner_repo_hooks_id_with_http_info(access_token, url, password, push_events,
                                                                            tag_push_events, issues_events, note_events,
                                                                            merge_requests_events, owner, repo, id,
                                                                            **kwargs)  # noqa: E501
            return data

    def patch_v5_repos_owner_repo_hooks_id_with_http_info(self, access_token, url, password, push_events,
                                                          tag_push_events, issues_events, note_events,
                                                          merge_requests_events, owner, repo, id,
                                                          **kwargs):  # noqa: E501
        """更新一个仓库WebHook  # noqa: E501

        更新一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_v5_repos_owner_repo_hooks_id_with_http_info(access_token, url, password, push_events, tag_push_events, issues_events, note_events, merge_requests_events, owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: (required)
        :param str url: (required)
        :param str password: (required)
        :param bool push_events: (required)
        :param bool tag_push_events: (required)
        :param bool issues_events: (required)
        :param bool note_events: (required)
        :param bool merge_requests_events: (required)
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'url', 'password', 'push_events', 'tag_push_events', 'issues_events',
                      'note_events', 'merge_requests_events', 'owner', 'repo', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_v5_repos_owner_repo_hooks_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError(
                "Missing the required parameter `access_token` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError(
                "Missing the required parameter `url` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError(
                "Missing the required parameter `password` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'push_events' is set
        if ('push_events' not in params or
                params['push_events'] is None):
            raise ValueError(
                "Missing the required parameter `push_events` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'tag_push_events' is set
        if ('tag_push_events' not in params or
                params['tag_push_events'] is None):
            raise ValueError(
                "Missing the required parameter `tag_push_events` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'issues_events' is set
        if ('issues_events' not in params or
                params['issues_events'] is None):
            raise ValueError(
                "Missing the required parameter `issues_events` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'note_events' is set
        if ('note_events' not in params or
                params['note_events'] is None):
            raise ValueError(
                "Missing the required parameter `note_events` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'merge_requests_events' is set
        if ('merge_requests_events' not in params or
                params['merge_requests_events'] is None):
            raise ValueError(
                "Missing the required parameter `merge_requests_events` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `patch_v5_repos_owner_repo_hooks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
            form_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'url' in params:
            form_params.append(('url', params['url']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501
        if 'push_events' in params:
            form_params.append(('push_events', params['push_events']))  # noqa: E501
        if 'tag_push_events' in params:
            form_params.append(('tag_push_events', params['tag_push_events']))  # noqa: E501
        if 'issues_events' in params:
            form_params.append(('issues_events', params['issues_events']))  # noqa: E501
        if 'note_events' in params:
            form_params.append(('note_events', params['note_events']))  # noqa: E501
        if 'merge_requests_events' in params:
            form_params.append(('merge_requests_events', params['merge_requests_events']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Hook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v5_repos_owner_repo_hooks(self, body, owner, repo, **kwargs):  # noqa: E501
        """创建一个仓库WebHook  # noqa: E501

        创建一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_hooks(body, owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body40 body: (required)
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v5_repos_owner_repo_hooks_with_http_info(body, owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.post_v5_repos_owner_repo_hooks_with_http_info(body, owner, repo, **kwargs)  # noqa: E501
            return data

    def post_v5_repos_owner_repo_hooks_with_http_info(self, body, owner, repo, **kwargs):  # noqa: E501
        """创建一个仓库WebHook  # noqa: E501

        创建一个仓库WebHook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_hooks_with_http_info(body, owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body40 body: (required)
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :return: Hook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'owner', 'repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v5_repos_owner_repo_hooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `post_v5_repos_owner_repo_hooks`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `post_v5_repos_owner_repo_hooks`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `post_v5_repos_owner_repo_hooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Hook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v5_repos_owner_repo_hooks_id_tests(self, owner, repo, id, **kwargs):  # noqa: E501
        """测试WebHook是否发送成功  # noqa: E501

        测试WebHook是否发送成功  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_hooks_id_tests(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param Body42 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v5_repos_owner_repo_hooks_id_tests_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_v5_repos_owner_repo_hooks_id_tests_with_http_info(owner, repo, id,
                                                                                 **kwargs)  # noqa: E501
            return data

    def post_v5_repos_owner_repo_hooks_id_tests_with_http_info(self, owner, repo, id, **kwargs):  # noqa: E501
        """测试WebHook是否发送成功  # noqa: E501

        测试WebHook是否发送成功  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v5_repos_owner_repo_hooks_id_tests_with_http_info(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: Webhook的ID (required)
        :param Body42 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v5_repos_owner_repo_hooks_id_tests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError(
                "Missing the required parameter `owner` when calling `post_v5_repos_owner_repo_hooks_id_tests`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError(
                "Missing the required parameter `repo` when calling `post_v5_repos_owner_repo_hooks_id_tests`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `post_v5_repos_owner_repo_hooks_id_tests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v5/repos/{owner}/{repo}/hooks/{id}/tests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
