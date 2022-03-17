<template>
  <div class="common-layout">
    <el-container>
      <el-header class="frens-header">Header</el-header>
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
            Fren id: {{ fren.id }}
            <br />
            Rarity score: {{ fren.rarityScore }}
            <br />
            <img :src="fren.img" />
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import type { FormInstance } from "element-plus";
import nftRarity from "@/assets/nft_rarity.json"; // TODO: transform into map instead of array for easier access

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
  const rarity = (nftRarity as Array<{id: string, rarity_score: number}>).find(x => x.id === frensId + '');


  if (typeof rarity === "undefined") {
    alert("Fren not found");
    return;
  }

  fren.value = {
    id: frensId,
    rarityScore: rarity.rarity_score,
    img: `https://stargaze.mypinata.cloud/ipfs/bafybeiaip3vwwhhgerw6gcs66clj4onubkdadquqzzpzrftvuyhgnzojse/images/${frensId}.jpg?img-width=600&img-fit=scale-down&img-anim=false&img-format=auto`,
  };
  /*
RarityScore/LowestRarityScore(MintPrice) = KRV

KRV4.679= X (present)
X6.11 = Y (future)

KARV = X range Y

RarityScore+5000/LowestRarityScore+5000(MintPrice)= KHRV

KHRV4.679=X (present)
X6.11=Y (future)

KHARV= X range Y

*/
}
</script>

<style>
.frens-header {
  text-align: center;
}
</style>
