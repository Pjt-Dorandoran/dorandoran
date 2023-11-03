package com.doran.admin_voice.dto.res;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class AdminVoiceResDtoList {
    // 해당 컨텐츠의 목소리 전원 반환할 때 필요
    private int size;
    private List<AdminVoiceResDto> adminVoiceResDtoList;
}