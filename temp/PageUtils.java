package com.jinquanquan.api.util;

import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class PageUtils {

    public static final String ASC = "asc";

    public static final String DESC = "desc";

    public Map<String, Object> getParams(
            Integer page, Integer size,
            String order, String direction) {
        if (page == null) {
            page = 0;
        }

        if (size == null) {
            size = 10;
        } else if (size > 100) {
            size = 100;
        }

        if (order == null) {
            order = "id";
        }

        if (direction == null) {
            direction = ASC;
        } else if (direction.equalsIgnoreCase(ASC)) {
            direction = ASC;
        } else if (direction.equalsIgnoreCase(DESC)) {
            direction = DESC;
        } else {
            direction = ASC;
        }

        Map<String, Object> params = new HashMap<String, Object>();
        params.put("page", page);
        params.put("size", size);
        params.put("offset", page * size);
        params.put("order", order);
        params.put("direction", direction);
        return params;
    }
}
