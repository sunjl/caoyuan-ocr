package com.jinquanquan.api.dto;

import java.util.List;

public class PageDto<T> {

    private Integer page;

    private Integer size;

    private Integer count;

    private List<T> items;

    public PageDto() {
    }

    public PageDto(Integer page, Integer size, Integer count, List<T> items) {
        this.page = page;
        this.size = size;
        this.count = count;
        this.items = items;
    }

    public Integer getPage() {
        return page;
    }

    public Integer getSize() {
        return size;
    }

    public Integer getCount() {
        return count;
    }

    public List<T> getItems() {
        return items;
    }

}
