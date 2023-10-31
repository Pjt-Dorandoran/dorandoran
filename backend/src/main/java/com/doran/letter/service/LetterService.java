package com.doran.letter.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.doran.letter.dto.req.LetterInsertDto;
import com.doran.letter.dto.res.LetterResDto;
import com.doran.letter.entity.Letter;
import com.doran.letter.mapper.LetterMapper;
import com.doran.letter.repository.LetterRepository;
import com.doran.parent.entity.Parent;
import com.doran.parent.service.ParentService;
import com.doran.profile.entity.Profile;
import com.doran.profile.repository.ProfileRepository;
import com.doran.profile.service.ProfileService;
import com.doran.utils.auth.Auth;
import com.doran.utils.bucket.mapper.BucketMapper;
import com.doran.utils.bucket.service.BucketService;
import com.doran.utils.common.UserInfo;
import com.doran.utils.exception.dto.CustomException;
import com.doran.utils.exception.dto.ErrorCode;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Service
@RequiredArgsConstructor
@Slf4j
public class LetterService{
    private final ParentService parentService; // 부모 아이 판별을 위해 import
    private final ProfileService profileService;
    private final BucketMapper bucketMapper;
    private final BucketService bucketService;
    private final LetterMapper letterMapper;
    private final LetterRepository letterRepository;
    // 부모한테 보낸 편지 조회
    public LetterResDto getParentLetter(int userId){
        Parent parent = parentService.findParentByUserId(userId);
        // List<Letter> result = letterRepository.findAllLetterByParentId(parent.getId());
        Letter letter = letterRepository.findLetterByParentId(parent.getId());
        LetterResDto letterResDto = letterMapper.parentLetterToResDto(letter);
        return letterResDto;
    }
    // 아이(Profile)한테 보낸 편지 조회
    public LetterResDto getChildLetter(int profileId){
        Profile profile = profileService.findProfileById(profileId);
        Letter letter = letterRepository.findLetterByProfileId(profileId);
        LetterResDto letterResDto = letterMapper.childLetterToResDto(letter);
        return letterResDto;
    }
    // 편지 등록
    public Letter insertLetter(LetterInsertDto letterInsertDto){
        UserInfo userInfo = Auth.getInfo();
        Parent parent = null;
        Profile profile = null;
        int receiverId=0, senderId=0;
        profile = profileService.findProfileById(letterInsertDto.getProfileId());
        if(parentService.checkParent(userInfo.getUserRole().getRole())){
            // 보내는 사람 프로필(아이), 받는 사람 부모일 때
            parent = parentService.findParentByProfileId(letterInsertDto.getProfileId());
            receiverId = parent.getId();
            senderId = profile.getId();
        }else{
            // 보내는 사람 부모, 받는 사람 프로필(아이)일 때
            parent = parentService.findParentByUserId(userInfo.getUserId());
            receiverId = profile.getId();
            senderId = parent.getId();
        }
        String contentUrl = bucketService.insertFile(bucketMapper.toInsertDto(letterInsertDto.getContent(), "letter"));
        Letter letter = letterMapper.insertLettertoLetter(letterInsertDto,parent,profile,contentUrl,receiverId,senderId);
        // 편지 저장 시 파일 이름
        return letterRepository.save(letter);
    }
}
