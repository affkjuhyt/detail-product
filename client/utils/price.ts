export function formatPrice(price: number) {
    const instance = new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND',
    });

    return instance.format(price);
}
