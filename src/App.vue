<template>
  <div class="common-layout">
    <el-container>
      <el-header class="frens-header">Frens rarity checker</el-header>
      <el-main>
        <el-row class="row-bg" justify="center">
          <el-col :span="6">
            <el-form
              @submit.prevent
              :model="checkForm"
              ref="formRef"
              label-width="120px"
            >
              <el-form-item
                label="Frens id"
                prop="frensId"
                :rules="[
                  { required: true, message: 'frens id is required' },
                  { type: 'number', message: 'frens id must be a number' },
                ]"
              >
                <el-input
                  v-model.number="checkForm.frensId"
                  type="text"
                  autocomplete="off"
                  v-on:keyup.enter="submitForm(formRef)"
                />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm(formRef)"
                  >Submit</el-button
                >
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
        <el-row v-if="fren" class="row-bg" justify="center">
          <el-col :span="6">
            <el-descriptions
                title="Estimated prices based on different algorithms"
                direction="horizontal"
                :column="1"
                size="large"
                border
            >
              <el-descriptions-item label="Fren id">{{ fren.id }}</el-descriptions-item>
              <el-descriptions-item label="Rarity score">{{ Math.round(fren.rarity_score) }}</el-descriptions-item>
              <el-descriptions-item label="KRV">{{ Math.round(fren.krv) }} Stars</el-descriptions-item>
              <el-descriptions-item label="KARV">{{ Math.round(fren.karv_present) }} Stars (today) - {{ Math.round(fren.karv_future) }} Stars (2 years from now)</el-descriptions-item>
              <el-descriptions-item label="KHRV">{{ Math.round(fren.khrv) }}</el-descriptions-item>
              <el-descriptions-item label="KHARV">{{ Math.round(fren.kharv_present) }} Stars (today) - {{ Math.round(fren.kharv_future) }} Stars (2 years from now)</el-descriptions-item>
            </el-descriptions>
            <el-image class="fren-image" :src="fren.img" />
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import type { FormInstance } from "element-plus";
import nftRarity from "@/assets/values.json"; // TODO: transform into map instead of array for easier access

const formRef = ref<FormInstance>();

const checkForm = reactive({
  frensId: "",
});

const fren = ref<any>(undefined);

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      check(checkForm.frensId);
    } else {
      return false;
    }
  });
};

function check(frensId: string) {
  const frenFound = (
    nftRarity as unknown as {
      [key: string]: {
        id: string | undefined;
        img: string | undefined;
        rarity_score: number;
        krv: number;
        karv_present: number;
        karv_future: number;
        khrv: number;
        kharv_present: number;
        kharv_future: number;
      };
    }
  )[frensId];

  if (typeof frenFound === "undefined") {
    alert("Fren not found");
    return;
  }

  frenFound.id = frensId;
  frenFound.img = `https://stargaze.mypinata.cloud/ipfs/bafybeiaip3vwwhhgerw6gcs66clj4onubkdadquqzzpzrftvuyhgnzojse/images/${frensId}.jpg?img-width=600&img-fit=scale-down&img-anim=false&img-format=auto`

  fren.value = frenFound;
}
</script>

<style>
@import "assets/base.css";

.frens-header {
  text-align: center;
  font-size: 32px;
}

.fren-image {
  margin-top: 25px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

</style>
