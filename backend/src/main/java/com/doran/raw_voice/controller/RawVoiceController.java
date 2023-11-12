package com.doran.raw_voice.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.doran.raw_voice.dto.req.CompleteInsertDto;
import com.doran.raw_voice.dto.req.RawVoiceInsertDto;
import com.doran.raw_voice.dto.req.TelInsertDto;
import com.doran.raw_voice.dto.res.RawVoiceListDto;
import com.doran.raw_voice.service.RawVoiceService;
import com.doran.record_book.entity.RecordBook;
import com.doran.record_book.service.RecordBookService;
import com.doran.redis.script.mapper.ScriptMapper;
import com.doran.redis.script.service.ScriptService;
import com.doran.redis.tel.service.TelService;
import com.doran.utils.auth.Auth;
import com.doran.utils.common.UserInfo;
import com.doran.utils.rabbitmq.service.ModelPubService;
import com.doran.utils.response.CommonResponseEntity;
import com.doran.utils.response.SuccessCode;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/voice")
@Slf4j
public class RawVoiceController {
    private final RawVoiceService rawVoiceService;
    private final TelService telService;
    private final ModelPubService modelPubService;
    private final ScriptService scriptService;
    private final RecordBookService recordBookService;
    private final ScriptMapper scriptMapper;

    @PreAuthorize("hasRole('ROLE_ADMIN')")
    @GetMapping("")
    public ResponseEntity<?> getRawVoiceList() {
        log.info("Raw Voice (원본 목소리) 리스트 호출");
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE, rawVoiceService.getRawVoiceAll());
    }

    // 유저 목소리 검색
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    @GetMapping("/{user_id}")
    public ResponseEntity<?> getRawVoiceListByUserId(@PathVariable(value = "user_id") int userId) {
        RawVoiceListDto rawVoiceListDto = rawVoiceService.getRawVoiceByUserId(userId);
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE, rawVoiceListDto);
    }

    // 원본 목소리 등록 (부모 실제 녹음)
    @PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_PARENT')") // 관리자, 부모만 등록 가능
    @PostMapping("")
    public ResponseEntity<?> insertRawVoice(RawVoiceInsertDto rawVoiceInsertDto) {
        log.info("Raw Voice (원본 목소리) 추가");
        UserInfo info = Auth.getInfo();

        rawVoiceService.insertRawVoice(rawVoiceInsertDto);

        //try-catch 바인딩 이후 제거 필요
        try {
            RecordBook script = recordBookService.findScript(rawVoiceInsertDto.getScript(),
                rawVoiceInsertDto.getScriptNum());
            scriptService.save(scriptMapper.toScript(info.getUserId(), script.getScript(), script.getScriptNum()));
        } catch (Exception e) {
            log.info("스크립트 안들어옴");
        }

        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE, null);
    }

    //녹음 완료 요청 API
    @PostMapping("/complete")
    @PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_PARENT')") // 관리자, 부모만 등록 가능
    public ResponseEntity<?> completeRecord(@RequestBody CompleteInsertDto completeInsertDto) {
        int userId = Auth.getInfo().getUserId();
        log.info("녹음 완료 요청 컨트롤러");
        log.info("녹음자 성별 : " + completeInsertDto.getGenders());
        modelPubService.sendMessage(userId, completeInsertDto.getGenders()); //model pub 호출
        log.info("해당 유저의 녹음이 완료되었습니다. " + userId);
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE);
    }

    //모델 생성시 알림이 갈 번호 등록
    @PostMapping("/tel")
    @PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_PARENT')") // 관리자, 부모만 등록 가능
    public ResponseEntity<?> insertTel(@RequestBody TelInsertDto telInsertDto) {
        log.info("번호 등록 컨트롤러");
        //redis 저장
        telService.save(Auth.getInfo().getUserId(), telInsertDto.getTel());
        return CommonResponseEntity.getResponseEntity(SuccessCode.SUCCESS_CODE);
    }
}
