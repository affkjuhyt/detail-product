import type { UseFetchOptions } from '#app';

export const useCustomFetch = (request: any, opts?: UseFetchOptions<any>) => {
    const runtimeConfig = useRuntimeConfig();
    const apiBaseUrl = runtimeConfig.serverApiBaseUrl || (runtimeConfig.public.apiBaseUrl as string);

    const params = {
        baseURL: apiBaseUrl,
        ...opts,
    } as UseFetchOptions<any>;

    return useFetch(request, params);
};
