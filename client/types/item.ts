import type { ResponseData } from '~/types/base';

export type ItemDetailRsp = ResponseData<ItemDetail>;

export type ItemDetail = {
    item: {
        id: number;
        slug: string;
        description: string;
        images: string[];
        historical_sold: number;
        rating_avg: number;
        price_before_discount: number;
        provider_url: string;
        updated_at: null;
        name: string;
        category_id: number;
        thumbnail: string;
        rating_count: number;
        comment_count: number;
        provider: string;
        created_at: Date;
        category: Category;
        categories: Category[];
        current_price: number;
    }
};

export type Category = {
    level: number;
    id: number;
    created_at: Date;
    name: string;
    slug: string;
    parent_id: number | null;
    updated_at: Date | null;
};

export type PriceHistory = {
    price: number;
    id: number;
    item_id: number;
    created_at: Date;
};

export type PriceHistoryRsp = ResponseData<PriceHistory[]>;
