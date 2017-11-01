package com.kuaizhizao.api.dto.common;

import com.google.common.base.CaseFormat;
import com.kuaizhizao.api.constant.CommonConstants;

public class PageRequestDto {

    private Integer page;

    private Integer size;

    private Integer offset;

    private String field;

    private String direction;

    private String sort;

    public PageRequestDto() {
    }

    public PageRequestDto(Integer page, Integer size, String field, String direction) {
        this.page = page;
        this.size = size;
        this.field = field;
        this.direction = direction;
        convert();
    }

    public PageRequestDto convert() {
        if (page == null) {
            page = 0;
        }

        if (size == null) {
            size = 10;
        } else if (size > 100) {
            size = 100;
        }

        offset = page * size;

        if (field != null) {
            field = CaseFormat.LOWER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, field);
            if (direction == null) {
                direction = CommonConstants.ASC;
                sort = field;
            } else if (direction.equalsIgnoreCase(CommonConstants.ASC)) {
                direction = CommonConstants.ASC;
                sort = field;
            } else if (direction.equalsIgnoreCase(CommonConstants.DESC)) {
                direction = CommonConstants.DESC;
                sort = CommonConstants.MINUS + field;
            } else {
                direction = CommonConstants.ASC;
                sort = field;
            }
        }
        return this;
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

    public Integer getOffset() {
        return offset;
    }

    public void setOffset(Integer offset) {
        this.offset = offset;
    }

    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public String getSort() {
        return sort;
    }

    public void setSort(String sort) {
        this.sort = sort;
    }
}
