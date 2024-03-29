import type { ResponseData } from '~/types/base';

export type CategoryData = {
    level: number;
    id: number;
    created_at: Date;
    slug: string;
    name: string;
    relative_path: string | null;
    url_thumbnail: string | null;
    parent_id: number | null;
    updated_at: Date | null;
    childs?: CategoryData[];
};

export type CategoriesRsp = ResponseData<CategoryData[]>;
