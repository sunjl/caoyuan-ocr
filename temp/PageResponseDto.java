package com.kuaizhizao.api.dto.common;

import java.util.List;

public class PageResponseDto<T> {

    private Integer page;

    private Integer size;

    private Long count;

    private List<T> items;

    public PageResponseDto() {
    }

    public PageResponseDto(Integer page, Integer size, Long count, List<T> items) {
        this.page = page;
        this.size = size;
        this.count = count;
        this.items = items;
    }

    public Integer getPage() {
        return page;
    }

    public void setPage(Integer page) {
        this.page = page;
    }

    public Integer getSize() {
        return size;
    }

    public void setSize(Integer size) {
        this.size = size;
    }

    public Long getCount() {
        return count;
    }

    public void setCount(Long count) {
        this.count = count;
    }

    public List<T> getItems() {
        return items;
    }

    public void setItems(List<T> items) {
        this.items = items;
    }
}
