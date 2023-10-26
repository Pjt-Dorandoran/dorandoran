package com.doran.content.controller;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.doran.content.dto.req.ContentInsertDto;
import com.doran.content.dto.res.ContentResDto;
import com.doran.content.service.ContentService;
import com.doran.page.entity.Page;
import com.doran.page.service.PageService;
import com.doran.utils.common.UserInfo;
import com.doran.utils.response.CommonResponseEntity;
import com.doran.utils.response.SuccessCode;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Controller
@RequestMapping("/api/content")
@RequiredArgsConstructor
@Slf4j
public class ContentController {
    private final ContentService contentService;
    private final PageService pageService;

    // 컨텐츠 등록
    @PostMapping("/{book_id}")
    ResponseEntity<?> insertContent(@PathVariable(value = "book_id") int bookId, @RequestBody ContentInsertDto contentInsertDto) {
        int idx = contentInsertDto.getIdx();
        String script = contentInsertDto.getScript();

        Page findPage = pageService.findPageIdByIdxAndBookId(bookId, idx);
        contentService.insertContent(findPage, script);
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE);
    }

    //컨텐츠 조회(동화 낭독), (동화책 Id, 페이지 idx)
    @GetMapping("/{book_id}/{idx}")
    ResponseEntity<?> getContent(@PathVariable(value = "book_id") int bookId, @PathVariable int idx) {
        UserInfo userInfo = (UserInfo)SecurityContextHolder.getContext()
            .getAuthentication()
            .getPrincipal();

        // 부모인지 아이인지 체킹
        // 아이라면 해당 부모의 UserId 끌고와야함 -> 일단 임시 땜빵
        int userId = 1;
        log.info("getContent 컨트롤러 호출");
        log.info("userId : " + userId);

        //idx로 pageId 추출 (idx)
        int pageId = pageService.findPageIdByIdxAndBookId(bookId, idx).getId();
        List<ContentResDto> findContent = contentService.getContentWithVoice(userId, pageId);
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE, findContent);
    }
}
